#!/usr/bin/env python3
"""Generate PDFs for visa documents using ghostscript ps2pdf."""
import os, subprocess, textwrap

PDF_DIR = os.path.expanduser("~/Desktop/pic/visa_quiz/pdf")
os.makedirs(PDF_DIR, exist_ok=True)

def make_pdf(filename, title, lines):
    """Create a simple PS file and convert to PDF via ps2pdf."""
    ps_path = os.path.join(PDF_DIR, filename + ".ps")
    pdf_path = os.path.join(PDF_DIR, filename + ".pdf")
    
    # Build simple PostScript
    ps = [
        "%!PS-Adobe-3.0",
        "/Courier findfont 10 scalefont setfont",
        "2 setlinewidth",
        "0 0 0 setrgbcolor",
    ]
    
    y = 780
    # Title
    ps.append(f"/Courier-Bold findfont 14 scalefont setfont")
    ps.append(f"40 {y} moveto ({title}) show")
    y -= 30
    ps.append(f"/Courier findfont 10 scalefont setfont")
    
    for line in lines:
        if line == "":
            y -= 14
            continue
        if line.startswith("# "):
            y -= 8
            ps.append(f"/Courier-Bold findfont 11 scalefont setfont")
            ps.append(f"40 {y} moveto ({line[2:]}) show")
            ps.append(f"/Courier findfont 10 scalefont setfont")
            y -= 18
            # underline
            ps.append(f"40 {y+2} 540 {y+2} 0.5 setlinewidth stroke")
        elif line.startswith("- "):
            txt = "  " + line
            ps.append(f"40 {y} moveto ({txt}) show")
            y -= 16
        else:
            # Word wrap
            wrapped = textwrap.wrap(line, width=80)
            for w in wrapped:
                if y < 40:
                    break
                ps.append(f"40 {y} moveto ({w}) show")
                y -= 14
        if y < 40:
            break
    
    ps.append("showpage")
    
    with open(ps_path, 'w') as f:
        f.write('\n'.join(ps))
    
    subprocess.run(['ps2pdf', ps_path, pdf_path], check=True)
    os.remove(ps_path)
    return pdf_path

# 1. Employment Letter Template
make_pdf("employment_letter_template", "EMPLOYMENT LETTER TEMPLATE / 在职证明模板", [
    "",
    "# EMPLOYMENT LETTER (English)",
    "",
    "[Company Letterhead]",
    "Date: _______________",
    "",
    "TO WHOM IT MAY CONCERN,",
    "",
    "This is to certify that Mr./Ms. [Name] (ID: [Passport No.])",
    "is employed at [Company Name] since [Start Date].",
    "",
    "Position: [Job Title]",
    "Monthly Salary: RMB [Amount]",
    "Annual Income: RMB [Amount]",
    "",
    "The applicant is granted leave from [Departure] to [Return]",
    "for traveling to [Country]. We guarantee the applicant will",
    "return to China on time and resume their position.",
    "",
    "Sincerely,",
    "",
    "[HR Manager Signature]      [Company Stamp]",
    "Tel: [Phone Number]",
    "",
    "------------------------------------------------------------",
    "",
    "# 中文在职证明",
    "",
    "[公司抬头纸]",
    "",
    "在职证明",
    "",
    "兹证明 [姓名] (身份证号：[ID]) 自 [入职日期] 起",
    "在我公司任职，现任 [职位]。",
    "",
    "月收入：人民币 [金额] 元",
    "年收入：人民币 [金额] 元",
    "",
    "该员工计划于 [出发日期] 至 [返回日期] 前往",
    "[目的地国家] 旅游/商务，所有费用由 [本人/公司] 承担。",
    "我公司保证其遵守当地法律，按时回国。",
    "",
    "______________________________",
    "[人力资源负责人签字]      [公司公章]",
    "日期：________",
    "联系电话：[Phone]",
])

# 2. Schengen Visa Guide
make_pdf("schengen_visa_guide", "SCHENGEN VISA APPLICATION GUIDE / 申根签证指南", [
    "",
    "# What is Schengen Visa?",
    "",
    "Allows travel in 29 European countries for up to 90 days",
    "within 180 days for tourism, business, or family visits.",
    "",
    "# Required Documents",
    "",
    "- Valid passport (6+ months, 2+ blank pages)",
    "- 3 passport photos (35x45mm, white bg)",
    "- Completed visa application form",
    "- Round-trip flight reservation",
    "- Hotel booking confirmation",
    "- Travel insurance (min 30,000 EUR coverage)",
    "- Bank statements (last 3-6 months)",
    "- Employment letter + business license copy",
    "- Property/vehicle documents (supporting)",
    "- ID card + household registration copy",
    "",
    "# Application Process",
    "",
    "Step 1: Determine main destination country",
    "Step 2: Prepare all documents",
    "Step 3: Book appointment at VAC (VFS/TLS/BDL)",
    "Step 4: Submit biometrics + documents",
    "Step 5: Pay visa fee (approx 80 EUR)",
    "Step 6: Wait 15-30 calendar days",
    "Step 7: Collect passport with decision",
    "",
    "# Tips for Success",
    "",
    "- Show consistent income in bank statements",
    "- Insurance must cover entire Schengen area",
    "- Flight/hotel reservations don't need payment",
    "- Be honest - false info = rejection",
    "- Family visit: include invitation letter + host's ID",
    "",
    "# Schengen Countries (29)",
    "",
    "Austria, Belgium, Bulgaria, Croatia, Czech Republic,",
    "Denmark, Estonia, Finland, France, Germany, Greece,",
    "Hungary, Iceland, Italy, Latvia, Liechtenstein,",
    "Lithuania, Luxembourg, Malta, Netherlands, Norway,",
    "Poland, Portugal, Romania, Slovakia, Slovenia,",
    "Spain, Sweden, Switzerland.",
])

# 3. US DS-160 Guide
make_pdf("us_visa_ds160_guide", "US VISA DS-160 FORM GUIDE / 美国DS-160指南", [
    "",
    "# Before You Start",
    "",
    "- Have passport ready (6+ months validity)",
    "- Digital photo (2x2 inch, white bg, within 6 months)",
    "- Know employment history (past 5 years)",
    "- Know travel history (past 5 years)",
    "- URL: https://ceac.state.gov/genniv/",
    "",
    "# Key Sections",
    "",
    "Personal Info: Name must match passport EXACTLY.",
    "Travel Info: Purpose (B1/B2), length of stay.",
    "Passport Info: Number, issue/expiry dates.",
    "Family Info: Parents' full names.",
    "Work/Education: Current and past 5 years.",
    "Security: ALL answered truthfully.",
    "",
    "# Common Mistakes",
    "",
    "- Name fields reversed (surname vs given name)",
    "- Wrong passport number",
    "- Inconsistent info between form and interview",
    "- Photo doesn't meet requirements",
    "- Losing confirmation number",
    "",
    "# After Submission",
    "",
    "1. Print DS-160 confirmation page (with barcode)",
    "2. Schedule interview at ais.usvisa-info.com",
    "3. Pay MRV fee ($185 for B1/B2)",
    "4. Bring: passport, confirmation, appointment letter,",
    "   fee receipt, photo, supporting docs",
    "5. Attend interview at US Embassy/Consulate",
    "6. Passport returned in 3-15 working days",
])

# 4. General Visa Checklist
make_pdf("visa_checklist_general", "GENERAL VISA CHECKLIST / 签证材料通用清单", [
    "",
    "# Core Documents (All Visas)",
    "",
    "- Valid passport (6+ months validity)",
    "- Passport photos (qty/size vary by country)",
    "- Completed visa application form (signed blue ink)",
    "- ID card copy (front and back)",
    "- Household registration (hukou) copy",
    "- Marriage certificate copy (if applicable)",
    "",
    "# Employment Documents",
    "",
    "- Employment letter (CN+EN, company letterhead)",
    "- Business license copy (company stamp)",
    "- 6 months bank statements (bank stamped)",
    "- Social insurance records (helpful)",
    "",
    "# Financial Documents",
    "",
    "- Bank deposit certificate (RMB 50K-100K+)",
    "- Property ownership certificate",
    "- Vehicle registration certificate",
    "- Stock/investment statements",
    "- Credit card statements",
    "",
    "# Travel Documents",
    "",
    "- Round-trip flight itinerary",
    "- Hotel booking confirmation",
    "- Travel insurance (Schengen: min 30K EUR)",
    "- Detailed travel itinerary",
    "",
    "# Special Cases",
    "",
    "Minors: birth cert, school letter, parents' consent",
    "Retirees: pension stmts, children's guarantee letter",
    "Students: enrollment letter, parents' financial docs",
    "Self-employed: license, tax records, company bank stmts",
    "Family visit: invitation letter, host's ID copy",
])

# 5. Service Brochure
make_pdf("bangde_visa_brochure", "BANGDE VISA BROCHURE / 帮得签证公司简介", [
    "",
    "BangDe Visa - Your Visa Assistant",
    "帮得签证 - 您的签证小管家",
    "",
    "# About Us",
    "",
    "Professional visa and travel service provider.",
    "One-stop visa solutions for tourism, business,",
    "family visits, and study abroad.",
    "",
    "# Our Services",
    "",
    "- Tourist Visa (US, UK, Schengen, Japan, AU, etc.)",
    "- Business Visa (expedited processing)",
    "- Family Visit Visa (invitation guidance)",
    "- Study Visa (F1, T4, Student visas)",
    "- Transit Visa (airport/seaport)",
    "- Work Visa (H1B, L1, Work Permits)",
    "",
    "# Why Choose BangDe?",
    "",
    "- Expert team with high success rates",
    "- Tailored visa strategy per applicant",
    "- Professional document review",
    "- Interview coaching & mock interviews",
    "- Real-time policy updates",
    "- 24/7 customer support",
    "",
    "# Contact",
    "",
    "WeChat Official Account: 帮得签证",
    "Service Available: Mon-Sun 9:00-21:00",
    "",
    "帮得签证 - 开启无忧旅程!",
])

print("All 5 PDFs created successfully in:", PDF_DIR)
