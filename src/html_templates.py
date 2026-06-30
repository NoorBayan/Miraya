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


def render_dashboard(stats, total_poems, era_name, theme_name):
    """
    قالب HTML لبناء لوحة تحكم إحصائية (Dashboard) تعرض تحليل الفاعلية والتشييء.
    """
    
    def make_progress_bar(label, count, total, color):
        percentage = (count / total) * 100 if total > 0 else 0
        return f"""
        <div style="margin-bottom: 15px;">
            <div style="display: flex; justify-content: space-between; font-size: 14px; margin-bottom: 5px; font-weight: bold; color: #2c3e50;">
                <span>{label}</span>
                <span>{count} ({percentage:.1f}%)</span>
            </div>
            <div style="width: 100%; background-color: #ecf0f1; border-radius: 8px; overflow: hidden; height: 18px; box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);">
                <div style="width: {percentage}%; background-color: {color}; height: 100%; border-radius: 8px;"></div>
            </div>
        </div>
        """

    obj_stats = stats.get('objectification', {})
    agency_stats = stats.get('agency', {})
    
    total_obj = sum(obj_stats.values())
    total_agency = sum(agency_stats.values())

    colors_obj = {'Fragmented': '#e74c3c', 'Holistic': '#3498db', 'Ornamental': '#9b59b6', 'Sensual': '#f39c12'}
    colors_agency = {'Speech Act': '#1abc9c', 'Emotional': '#e67e22', 'Social/Political': '#34495e', 'Domestic': '#f1c40f', 'Intellectual': '#8e44ad'}

    html = f"""
    <div dir="rtl" style="font-family: 'Segoe UI', Tahoma, Arial, sans-serif; background-color: #f8f9fa; border: 1px solid #dcdde1; border-radius: 12px; padding: 25px; max-width: 950px; margin: auto; box-shadow: 0 8px 16px rgba(0,0,0,0.1);">
        
        <!-- Header -->
        <div style="background: linear-gradient(135deg, #16a085, #2ecc71); color: white; padding: 20px; border-radius: 10px; margin-bottom: 25px; text-align: center;">
            <h2 style="margin: 0; font-size: 26px;">📊 لوحة التحليل الكمي (Distant Reading Dashboard)</h2>
            <p style="margin: 10px 0 0 0; font-size: 16px;">
                تم تحليل <b>{total_poems:,}</b> قصيدة بناءً على: العصر [<b>{era_name}</b>] | الغرض [<b>{theme_name}</b>]
            </p>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 25px;">
            
            <!-- Card 1: Objectification -->
            <div style="background: white; padding: 20px; border-radius: 10px; border: 1px solid #e1e8ed; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
                <h3 style="color: #c0392b; margin-top: 0; border-bottom: 2px solid #fadbd8; padding-bottom: 10px;">👁️ أنماط التشييء (Objectification)</h3>
                <p style="font-size: 13px; color: #7f8c8d; margin-bottom: 20px;">إجمالي الحالات المكتشفة: {total_obj:,}</p>
                {"".join([make_progress_bar(k, v, total_obj, colors_obj.get(k, '#95a5a6')) for k, v in obj_stats.items() if k not in ['None', 'N/A']])}
                {f'<div style="text-align:center; padding:10px; color:#7f8c8d; font-style:italic;">لا توجد بيانات تشييء كافية.</div>' if total_obj == 0 else ''}
            </div>

            <!-- Card 2: Agency Fields -->
            <div style="background: white; padding: 20px; border-radius: 10px; border: 1px solid #e1e8ed; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
                <h3 style="color: #2980b9; margin-top: 0; border-bottom: 2px solid #d6eaf8; padding-bottom: 10px;">⚡ مجالات الفاعلية (Agency)</h3>
                <p style="font-size: 13px; color: #7f8c8d; margin-bottom: 20px;">إجمالي الحالات المكتشفة: {total_agency:,}</p>
                {"".join([make_progress_bar(k, v, total_agency, colors_agency.get(k, '#95a5a6')) for k, v in agency_stats.items() if k not in ['None', 'N/A']])}
                {f'<div style="text-align:center; padding:10px; color:#7f8c8d; font-style:italic;">لا توجد بيانات فاعلية كافية.</div>' if total_agency == 0 else ''}
            </div>
            
        </div>
        
        <div style="margin-top: 20px; background: #fff3cd; color: #856404; padding: 15px; border-radius: 8px; border-left: 5px solid #ffeeba; font-size: 14px;">
            💡 <b>ملاحظة بحثية:</b> تتيح هذه اللوحة قراءة الأنماط السائدة دون الحاجة لقراءة النصوص الفردية، مما يسهل رصد التغيرات التاريخية في تمثيل الجندر.
        </div>
    </div>
    """
    return html

def render_interaction_network(triples_data, total_extracted, era_name, theme_name):
    """
    قالب HTML لبناء جدول شبكي (Network Viewer) يعرض العلاقات الدلالية
    بين المشاركين في القصيدة (Subject -> Gaze/Action -> Object).
    """
    
    # تنسيق رأس اللوحة
    html = f"""
    <div dir="rtl" style="font-family: 'Segoe UI', Tahoma, Arial, sans-serif; background-color: #f8f9fa; border: 1px solid #dcdde1; border-radius: 12px; padding: 25px; max-width: 950px; margin: auto; box-shadow: 0 8px 16px rgba(0,0,0,0.1);">
        
        <!-- Header -->
        <div style="background: linear-gradient(135deg, #8e44ad, #9b59b6); color: white; padding: 20px; border-radius: 10px; margin-bottom: 25px; text-align: center;">
            <h2 style="margin: 0; font-size: 26px;">🕸️ شبكة التفاعلات والنظرة (Interaction & Gaze Network)</h2>
            <p style="margin: 10px 0 0 0; font-size: 15px;">
                تم استخراج <b>{total_extracted:,}</b> مسار علائقي (Triple) بناءً على: العصر [<b>{era_name}</b>] | الغرض [<b>{theme_name}</b>]
            </p>
        </div>
        
        <div style="background: white; border-radius: 10px; border: 1px solid #e1e8ed; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
            <table style="width: 100%; border-collapse: collapse; text-align: center;">
                <thead>
                    <tr style="background-color: #34495e; color: white;">
                        <th style="padding: 12px; font-size: 16px; width: 25%;">الفاعل (Subject Node)</th>
                        <th style="padding: 12px; font-size: 16px; width: 10%;"></th>
                        <th style="padding: 12px; font-size: 16px; width: 30%;">العلاقة الدلالية (Edge)</th>
                        <th style="padding: 12px; font-size: 16px; width: 10%;"></th>
                        <th style="padding: 12px; font-size: 16px; width: 25%;">المتلقي (Object Node)</th>
                    </tr>
                </thead>
                <tbody>
    """

    # تنسيق صفوف الجدول (Triples)
    for idx, t in enumerate(triples_data):
        bg_color = "#f9f9f9" if idx % 2 == 0 else "#ffffff"
        
        # ألوان للتمييز بناءً على اتجاه النظرة أو الفاعل
        edge_color = "#2c3e50"
        edge_bg = "#ecf0f1"
        if t['relation'] == 'Male-to-Female':
            edge_color = "#c0392b"
            edge_bg = "#fadbd8"
        elif t['relation'] == 'Female-to-Male':
            edge_color = "#2980b9"
            edge_bg = "#d6eaf8"
        elif t['relation'] == 'Self-Gaze':
            edge_color = "#27ae60"
            edge_bg = "#d4efdf"
            
        html += f"""
                <tr style="background-color: {bg_color}; border-bottom: 1px solid #ecf0f1;">
                    <td style="padding: 15px; font-weight: bold; color: #2c3e50;">{t['subject']}</td>
                    <td style="padding: 15px; color: #bdc3c7;">←</td>
                    <td style="padding: 15px;">
                        <span style="background-color: {edge_bg}; color: {edge_color}; padding: 5px 15px; border-radius: 20px; font-size: 13px; font-weight: bold; border: 1px solid {edge_color}40;">
                            {t['relation']}
                        </span>
                        <div style="font-size: 11px; color: #7f8c8d; margin-top: 5px;">( ID: {t['poem_id']} )</div>
                    </td>
                    <td style="padding: 15px; color: #bdc3c7;">→</td>
                    <td style="padding: 15px; font-weight: bold; color: #2c3e50;">{t['object']}</td>
                </tr>
        """
        
    html += """
                </tbody>
            </table>
        </div>
        
        <div style="margin-top: 20px; background: #e8f8f5; color: #117a65; padding: 15px; border-radius: 8px; border-left: 5px solid #1abc9c; font-size: 14px;">
            💡 <b>ملاحظة بحثية:</b> يعكس هذا الجدول كيفية تحويل النص الشعري الحر إلى (Knowledge Graph). كل سطر يمثل مساراً منطقياً قابلاً للقراءة الآلية (Machine-Actionable Semantic Triple).
        </div>
    </div>
    """
    return html

def render_diachronic_tracker(trend_data, phenomenon_name, max_percentage):
    """
    قالب HTML لبناء مخطط زمني بياني (Timeline Bar Chart) لتتبع تطور ظاهرة عبر العصور.
    """
    
    html = f"""
    <div dir="rtl" style="font-family: 'Segoe UI', Tahoma, Arial, sans-serif; background-color: #f8f9fa; border: 1px solid #dcdde1; border-radius: 12px; padding: 25px; max-width: 950px; margin: auto; box-shadow: 0 8px 16px rgba(0,0,0,0.1);">
        
        <!-- Header -->
        <div style="background: linear-gradient(135deg, #2980b9, #3498db); color: white; padding: 20px; border-radius: 10px; margin-bottom: 25px; text-align: center; position: relative; overflow: hidden;">
            <h2 style="margin: 0; font-size: 26px; position: relative; z-index: 2;">📈 التتبع التاريخي للظواهر (Diachronic Trend Tracker)</h2>
            <p style="margin: 10px 0 0 0; font-size: 16px; position: relative; z-index: 2;">
                تتبع تطور ظاهرة: <span style="background: #f1c40f; color: #2c3e50; padding: 2px 10px; border-radius: 15px; font-weight: bold;">{phenomenon_name}</span> عبر العصور الأدبية
            </p>
        </div>

        <!-- The Timeline Chart -->
        <div style="background: white; padding: 25px; border-radius: 10px; border: 1px solid #e1e8ed; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
            <div style="display: flex; border-bottom: 2px solid #ecf0f1; padding-bottom: 10px; margin-bottom: 15px; font-weight: bold; color: #7f8c8d; font-size: 14px;">
                <div style="width: 25%;">العصر الأدبي (Chronological)</div>
                <div style="width: 60%;">التردد النسبي للظاهرة (Relative Frequency)</div>
                <div style="width: 15%; text-align: left;">الأعداد (Count)</div>
            </div>
    """

    # رسم الأعمدة البيانية لكل عصر
    for era in trend_data:
        era_name = era['era_name']
        count = era['count']
        total = era['total']
        percentage = era['percentage']
        
        # حساب العرض النسبي للشريط (بالنسبة لأعلى قيمة ليكون الرسم متناسقاً)
        bar_width = (percentage / max_percentage * 100) if max_percentage > 0 else 0
        
        # تدرج لوني يعتمد على كثافة الظاهرة (أحمر للكثيف، أزرق للقليل)
        color = "#e74c3c" if percentage > (max_percentage * 0.7) else ("#f39c12" if percentage > (max_percentage * 0.4) else "#3498db")
        
        html += f"""
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <!-- Era Name -->
                <div style="width: 25%; font-weight: bold; color: #2c3e50; font-size: 14px;">
                    {era_name}
                </div>
                
                <!-- Progress Bar -->
                <div style="width: 60%; padding-left: 15px;">
                    <div style="display: flex; align-items: center; height: 24px;">
                        <div style="width: {bar_width}%; background-color: {color}; height: 100%; border-radius: 4px; transition: width 1s ease-in-out; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"></div>
                        <span style="margin-right: 10px; font-size: 13px; font-weight: bold; color: {color};">{percentage:.1f}%</span>
                    </div>
                </div>
                
                <!-- Raw Numbers -->
                <div style="width: 15%; text-align: left; font-size: 12px; color: #95a5a6; background: #f8f9fa; padding: 4px; border-radius: 4px; border: 1px solid #ecf0f1;">
                    {count} / {total}
                </div>
            </div>
        """

    html += """
        </div>
        
        <!-- Research Insight -->
        <div style="margin-top: 20px; background: #e8f6f3; color: #0e6251; padding: 15px; border-radius: 8px; border-left: 5px solid #1abc9c; font-size: 14px; line-height: 1.6;">
            💡 <b>منهجية البحث (Methodological Note):</b> لتجنب الانحياز الإحصائي الناتج عن تفاوت عدد القصائد بين العصور (مثلاً العصر العباسي أضخم بكثير من غيره)، يعتمد هذا المخطط على <b>التردد النسبي (Percentages)</b> وليس الأعداد المطلقة. هذا يضمن قراءة علمية دقيقة لكيفية تطور الظاهرة كـ "نسبة مئوية من إجمالي الإنتاج الشعري" لكل عصر.
        </div>
    </div>
    """
    return html
