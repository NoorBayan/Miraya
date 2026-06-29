# ==============================================================================
# File: html_templates.py
# Description: Master HTML templates for Colab rendering.
# ==============================================================================

def render_semantic_explorer(poem, decoded_meta):
    """
    قالب HTML متقدم وعالي الاحترافية لعرض كافة التفاصيل الدلالية والشكلية للقصيدة.
    """
    # استخراج البيانات الفرعية
    content = poem.get('content', {})
    prosody = poem.get('metadata', {}).get('prosody', {})
    semantic = poem.get('semantic_analysis', {})
    main_evt = semantic.get('main_event', {})
    roles = poem.get('participants_and_roles', {})
    lit = poem.get('literary_analytics_and_review', {})
    qc = lit.get('quality_control', {})
    
    poem_text = content.get('poem_text', 'النص غير متوفر')
    
    # بناء القالب
    html = f"""
    <div dir="rtl" style="font-family: 'Segoe UI', Tahoma, Arial, sans-serif; background-color: #f4f6f9; border: 1px solid #dcdde1; border-radius: 12px; padding: 25px; box-shadow: 0 10px 20px rgba(0,0,0,0.05); max-width: 950px; margin: auto;">
        
        <!-- Header (Metadata & Prosody) -->
        <div style="background: linear-gradient(135deg, #2c3e50, #34495e); color: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h2 style="margin: 0 0 10px 0; font-size: 24px; color: #f1c40f;">{decoded_meta['title']}</h2>
                <div style="font-size: 14px; line-height: 1.8;">
                    <span>👤 الشاعر: <b>{decoded_meta['poet_name']}</b> ({decoded_meta['gender']})</span> | 
                    <span>⏳ العصر: <b>{decoded_meta['era']}</b></span> | 
                    <span>🌍 البلد: <b>{decoded_meta['country']}</b></span><br>
                    <span>📜 الغرض: <b>{decoded_meta['theme']}</b></span> | 
                    <span>🎼 البحر: <b>{decoded_meta['meter']}</b></span> | 
                    <span>🎵 القافية: <b>{decoded_meta['rhyme']}</b></span>
                </div>
            </div>
            <div style="text-align: left;">
                <span style="background: rgba(255,255,255,0.2); padding: 5px 15px; border-radius: 20px; font-size: 14px; letter-spacing: 1px;">ID: {poem.get('metadata',{}).get('poem_id')}</span>
            </div>
        </div>

        <!-- Poem Text -->
        <div style="text-align: center; background: white; padding: 30px 20px; border-radius: 10px; border-right: 5px solid #3498db; margin-bottom: 25px; box-shadow: 0 2px 5px rgba(0,0,0,0.02);">
            <h2 style="color: #2980b9; margin: 0; line-height: 1.8; font-size: 26px;">"{poem_text}"</h2>
        </div>

        <!-- 3-Column Grid for Deep Analytics -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 20px;">
            
            <!-- Column 1: Main Event -->
            <div style="background: white; padding: 15px; border-radius: 10px; border: 1px solid #e1e8ed;">
                <h4 style="color: #e67e22; margin-top: 0; border-bottom: 2px solid #fcf3cf; padding-bottom: 8px;">🎯 الحدث المحوري</h4>
                <p style="font-size: 14px; color: #34495e; font-weight: bold;">{main_evt.get('description', 'غير محدد')}</p>
                <hr style="border: 0; border-top: 1px dashed #ecf0f1;">
                <p style="margin: 5px 0; font-size: 13px;"><b>الجذر (Lemma):</b> <span style="color:#d35400;">{main_evt.get('verb_lemma', '-')}</span></p>
                <p style="margin: 5px 0; font-size: 13px;"><b>الزمن (Tense):</b> {main_evt.get('tense', '-')} | <b>الصيغة:</b> {main_evt.get('mood', '-')}</p>
                <p style="margin: 5px 0; font-size: 13px;"><b>القطبية (Polarity):</b> {main_evt.get('polarity', '-')}</p>
            </div>

            <!-- Column 2: Roles & Participants -->
            <div style="background: white; padding: 15px; border-radius: 10px; border: 1px solid #e1e8ed;">
                <h4 style="color: #8e44ad; margin-top: 0; border-bottom: 2px solid #f4ecf7; padding-bottom: 8px;">👥 الأدوار الدلالية</h4>
                <p style="margin: 5px 0; font-size: 13px;"><b>المرأة الأبرز:</b> <span style="background:#fadbd8; color:#c0392b; padding:2px 6px; border-radius:4px;">{roles.get('primary_roles', {}).get('woman', 'لا يوجد')}</span></p>
                <p style="margin: 5px 0; font-size: 13px;"><b>الرجل الأبرز:</b> <span style="background:#d6eaf8; color:#2980b9; padding:2px 6px; border-radius:4px;">{roles.get('primary_roles', {}).get('man', 'لا يوجد')}</span></p>
                <p style="margin: 15px 0 5px 0; font-size: 13px;"><b>أساس استنتاج الجنس:</b><br> <span style="color:#7f8c8d; font-style:italic;">{roles.get('gender_inference_basis', '-')}</span></p>
            </div>

            <!-- Column 3: Literary & Gaze -->
            <div style="background: white; padding: 15px; border-radius: 10px; border: 1px solid #e1e8ed;">
                <h4 style="color: #27ae60; margin-top: 0; border-bottom: 2px solid #e8f8f5; padding-bottom: 8px;">🎭 تحليل التشييء والفاعلية</h4>
                <p style="margin: 5px 0; font-size: 13px;"><b>اتجاه النظرة (Gaze):</b> <b>{lit.get('gaze_direction', '-')}</b></p>
                <p style="margin: 5px 0; font-size: 13px;"><b>نوع التشييء:</b> <span style="background:#fcf3cf; padding:2px 6px; border-radius:4px;">{lit.get('objectification_type', '-')}</span></p>
                <p style="margin: 5px 0; font-size: 13px;"><b>مجال الفاعلية:</b> <span style="background:#eaeded; padding:2px 6px; border-radius:4px;">{lit.get('agency_type', '-')}</span></p>
                <p style="margin: 10px 0 0 0; font-size: 13px;"><b>الوسوم (Tags):</b> {', '.join(lit.get('thematic_tags', []))}</p>
            </div>
        </div>

        <!-- Footer: Event Summary & Quality Control -->
        <div style="background: white; padding: 15px; border-radius: 10px; border: 1px solid #e1e8ed; display: flex; flex-direction: column; gap: 10px;">
            <div style="font-size: 14px;">
                <b style="color:#34495e;">📝 الملخص الدلالي:</b> {lit.get('event_summary', 'لا يوجد ملخص متاح.')}
            </div>
            <div style="border-top: 1px solid #f2f3f4; padding-top: 10px; display: flex; justify-content: space-between; font-size: 12px;">
                <span><b>مستوى الثقة:</b> <span style="color: {'green' if qc.get('confidence')=='High' else 'orange'};">{qc.get('confidence', '-')}</span></span>
                <span><b>تنبيهات المراجعة (Flags):</b> <span style="color: #c0392b;">{' | '.join(qc.get('review_flags', ['لا يوجد']))}</span></span>
            </div>
        </div>

    </div>
    """
    return html
