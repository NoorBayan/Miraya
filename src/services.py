# ==============================================================================
# File: services.py
# Description: Connects data and mappings to HTML templates.
# ==============================================================================

import random
from src.mappings import *
from src.html_templates import render_semantic_explorer

def service_semantic_explorer(filtered_data):
    """الخدمة الأولى: تختار قصيدة عشوائية من الداتا המفلترة، تفك شفرتها، وتعرضها"""
    
    if not filtered_data:
        return "<div style='text-align:center; padding:20px; color:red; font-weight:bold; background:#fadbd8; border-radius:8px;'>⚠️ لا توجد قصائد تطابق الفلاتر المحددة. جرب تغيير العصر أو الموضوع.</div>"
    
    # اختيار قصيدة
    poem = random.choice(filtered_data)
    
    # فك تشفير البيانات الوصفية (Metadata Decoding)
    meta = poem.get('metadata', {})
    poet = meta.get('poet', {})
    info = meta.get('poem_info', {})
    pros = meta.get('prosody', {})
    
    decoded_meta = {
        'poem_id': meta.get('poem_id', 'N/A'),
        'title': info.get('title', 'بدون عنوان'),
        'poet_name': poet.get('name', 'غير معروف'),
        'gender': get_name(gender_dic, poet.get('gender')),
        'era': get_name(poet_era_dic, poet.get('era')),
        'country': get_name(poet_location_dic, poet.get('country')),
        'theme': get_name(theme_dic, info.get('theme_id')),
        'meter': get_name(main_meter_dic, pros.get('main_meter')),
        'rhyme': get_name(rhyme_dic, pros.get('rhyme'))
    }
    
    # تمرير البيانات للقالب
    return render_semantic_explorer(poem, decoded_meta)


from collections import Counter
from src.html_templates import render_dashboard

def service_analytics_dashboard(filtered_data, era_name, theme_name):
    """
    الخدمة الثانية: تجميع إحصائيات التشييء والفاعلية للعينة المحددة وإرسالها لداشبورد.
    """
    if not filtered_data:
        return "<div style='text-align:center; padding:20px; color:red; font-weight:bold; background:#fadbd8; border-radius:8px; max-width:950px; margin:auto;'>⚠️ لا توجد قصائد تطابق الفلاتر المحددة. جرب تغيير العصر أو الموضوع.</div>"
    
    obj_counter = Counter()
    agency_counter = Counter()
    
    for poem in filtered_data:
        lit = poem.get('literary_analytics_and_review', {})
        
        obj_type = lit.get('objectification_type')
        agency_type = lit.get('agency_type')
        
        if obj_type and obj_type not in ['N/A', 'None']:
            obj_counter[obj_type] += 1
            
        if agency_type and agency_type not in ['N/A', 'None']:
            agency_counter[agency_type] += 1

    stats = {
        'objectification': dict(obj_counter.most_common()),
        'agency': dict(agency_counter.most_common())
    }
    
    return render_dashboard(stats, len(filtered_data), era_name, theme_name)


from src.html_templates import render_interaction_network

def service_interaction_network(filtered_data, era_name, theme_name):
    """
    الخدمة الثالثة: تقوم باستخراج العلاقات الثلاثية (Triples) من الأبيات لعرضها كشبكة.
    """
    if not filtered_data:
        return "<div style='text-align:center; padding:20px; color:red; font-weight:bold; background:#fadbd8; border-radius:8px; max-width:950px; margin:auto;'>⚠️ لا توجد قصائد تطابق الفلاتر المحددة. جرب تغيير العصر أو الموضوع.</div>"
    
    triples_list = []
    
    # 1. استخراج العلاقات (Triples)
    for poem in filtered_data:
        roles = poem.get('participants_and_roles', {}).get('primary_roles', {})
        lit = poem.get('literary_analytics_and_review', {})
        poem_id = poem.get('metadata', {}).get('poem_id', 'N/A')
        
        subject_man = roles.get('man', 'رجل (غير محدد)')
        object_woman = roles.get('woman', 'امرأة (غير محددة)')
        gaze = lit.get('gaze_direction')
        
        # فلترة العلاقات الواضحة فقط
        if gaze and gaze not in ['None', 'N/A']:
            triple = {
                'poem_id': poem_id,
                'relation': gaze
            }
            
            # تحديد الفاعل والمفعول بناءً على اتجاه النظرة
            if gaze == 'Male-to-Female':
                triple['subject'] = subject_man
                triple['object'] = object_woman
            elif gaze == 'Female-to-Male':
                triple['subject'] = object_woman
                triple['object'] = subject_man
            elif gaze == 'Self-Gaze':
                # افتراضياً المتكلم يصف نفسه، نحتاج لمعرفة جنسه
                speaker_gender = poem.get('participants_and_roles', {}).get('speaker', {}).get('gender', 'Unknown')
                subject_name = subject_man if speaker_gender == 'Male' else object_woman
                triple['subject'] = subject_name
                triple['object'] = "نفسه/نفسها"
            elif gaze == 'Mutual':
                triple['subject'] = f"{subject_man} & {object_woman}"
                triple['object'] = "تبادل النظرة/الفعل"
            else:
                continue # تخطي الحالات غير الواضحة
                
            triples_list.append(triple)

    # 2. عرض عينة فقط إذا كانت القائمة كبيرة جداً (لمنع انهيار المتصفح)
    total_extracted = len(triples_list)
    sample_size = min(15, total_extracted) # عرض 15 مسار كحد أقصى للديمو
    
    if total_extracted == 0:
         return "<div style='text-align:center; padding:20px; color:#856404; font-weight:bold; background:#fff3cd; border-radius:8px; max-width:950px; margin:auto;'>⚠️ لم يتم العثور على علاقات (Gaze) صريحة في هذه العينة لبناء الشبكة.</div>"

    # خلط العينة لعرض أمثلة متنوعة
    import random
    sampled_triples = random.sample(triples_list, sample_size)
    
    return render_interaction_network(sampled_triples, total_extracted, era_name, theme_name)
