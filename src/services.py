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

def service_analytics_dashboard(filtered_data, era_name, theme_name):
    """
    الخدمة الثانية: تقوم بتجميع إحصائيات التشييء والفاعلية للعينة المحددة وإرسالها لداشبورد.
    """
    if not filtered_data:
        return "<div style='text-align:center; padding:20px; color:red; font-weight:bold; background:#fadbd8; border-radius:8px;'>⚠️ لا توجد قصائد تطابق الفلاتر المحددة. جرب تغيير العصر أو الموضوع.</div>"
    
    # 1. إعداد العدادات (Counters)
    obj_counter = Counter()
    agency_counter = Counter()
    
    # 2. تجميع البيانات
    for poem in filtered_data:
        lit = poem.get('literary_analytics_and_review', {})
        
        obj_type = lit.get('objectification_type')
        agency_type = lit.get('agency_type')
        
        if obj_type and obj_type not in ['N/A', 'None']:
            obj_counter[obj_type] += 1
            
        if agency_type and agency_type not in ['N/A', 'None']:
            agency_counter[agency_type] += 1

    # 3. ترتيب النتائج من الأعلى للأقل لسهولة القراءة
    stats = {
        'objectification': dict(obj_counter.most_common()),
        'agency': dict(agency_counter.most_common())
    }
    
    # استدعاء قالب داشبورد (يجب استيراده في أعلى ملف services.py)
    # تذكر إضافة: from src.html_templates import render_dashboard
    from src.html_templates import render_dashboard
    return render_dashboard(stats, len(filtered_data), era_name, theme_name)
