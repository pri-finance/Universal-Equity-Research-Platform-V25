import pandas as pd
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Image

# LOAD EXCEL FILE

file_path = input("Enter Excel File Path: ")

import os

if not os.path.exists(file_path):
    print("File Not Found")
    exit()

df = pd.read_excel(file_path)

# COMPANY NAME

company_name = df.loc[
    df["Metric"] == "Company Name",
    "FY2026"
].values[0]

print("=" * 60)
print(company_name, "EQUITY RESEARCH ENGINE V24")
print("=" * 60)

# FY2026 DATA

revenue_2026 = df.loc[
    df["Metric"] == "Revenue ($B)",
    "FY2026"
].values[0]

net_income_2026 = df.loc[
    df["Metric"] == "Net Income ($B)",
    "FY2026"
].values[0]

assets_2026 = df.loc[
    df["Metric"] == "Total Assets ($B)",
    "FY2026"
].values[0]

equity_2026 = df.loc[
    df["Metric"] == "Shareholders Equity ($B)",
    "FY2026"
].values[0]

fcf_2026 = df.loc[
    df["Metric"] == "Free Cash Flow ($B)",
    "FY2026"
].values[0]

print("\nFINANCIAL OVERVIEW")

print("Revenue:", revenue_2026)
print("Net Income:", net_income_2026)
print("Assets:", assets_2026)
print("Equity:", equity_2026)
print("FCF:", fcf_2026)

# CALCULATED METRICS

roe = net_income_2026 / equity_2026

roa = net_income_2026 / assets_2026

print("\nCALCULATED METRICS")

print("ROE:", round(roe * 100, 2), "%")

print("ROA:", round(roa * 100, 2), "%")

# BUSINESS SCORING

score = 0

if roe > 0.20:
    score += 1

if roa > 0.10:
    score += 1

if revenue_2026 > 100:
    score += 1

if net_income_2026 > 20:
    score += 1

if fcf_2026 > 0:
    score += 1

print("\nBUSINESS SCORING")

print("Business Score:", score, "/ 5")

# FY2022 DATA

revenue_2022 = df.loc[
    df["Metric"] == "Revenue ($B)",
    "FY2022"
].values[0]

net_income_2022 = df.loc[
    df["Metric"] == "Net Income ($B)",
    "FY2022"
].values[0]

assets_2022 = df.loc[
    df["Metric"] == "Total Assets ($B)",
    "FY2022"
].values[0]

equity_2022 = df.loc[
    df["Metric"] == "Shareholders Equity ($B)",
    "FY2022"
].values[0]

fcf_2022 = df.loc[
    df["Metric"] == "Free Cash Flow ($B)",
    "FY2022"
].values[0]

revenue_cagr = (
    (revenue_2026 / revenue_2022) ** (1/4) - 1
) * 100

net_income_cagr = (
    (net_income_2026 / net_income_2022) ** (1/4) - 1
) * 100

assets_cagr = (
    (assets_2026 / assets_2022) ** (1/4) - 1
) * 100

equity_cagr = (
    (equity_2026 / equity_2022) ** (1/4) - 1
) * 100

fcf_cagr = (
    (fcf_2026 / fcf_2022) ** (1/4) - 1
) * 100

print("\nGROWTH ANALYSIS")

print("Revenue CAGR:", round(revenue_cagr, 2), "%")

print("Net Income CAGR:", round(net_income_cagr, 2), "%")

print("Assets CAGR:", round(assets_cagr, 2), "%")

print("Equity CAGR:", round(equity_cagr, 2), "%")

print("FCF CAGR:", round(fcf_cagr, 2), "%")

growth_score = 0

if revenue_cagr > 15:
    growth_score += 1

if net_income_cagr > 15:
    growth_score += 1

if assets_cagr > 10:
    growth_score += 1

if equity_cagr > 10:
    growth_score += 1

if fcf_cagr > 10:
    growth_score += 1

print("\nGROWTH SCORE")

print("Growth Score:", growth_score, "/ 5")

total_score = score + growth_score

print("\nTOTAL SCORE")

print("Total Score:", total_score, "/ 10")

if total_score >= 9:
    grade = "A+"

elif total_score >= 8:
    grade = "A"

elif total_score >= 6:
    grade = "B"

elif total_score >= 4:
    grade = "C"

else:
    grade = "D"

print("\nGRADE")

print("Grade:", grade)

if total_score >= 9:
    verdict = "Exceptional Business"

elif total_score >= 7:
    verdict = "Strong Business"

elif total_score >= 5:
    verdict = "Good Business"

else:
    verdict = "Weak Business"

print("\nFINAL VERDICT")

print("Verdict:", verdict)

if total_score >= 9:
    recommendation = "STRONG BUY"

elif total_score >= 7:
    recommendation = "BUY"

elif total_score >= 5:
    recommendation = "HOLD"

else:
    recommendation = "AVOID"

print("\nRECOMMENDATION")

print("Recommendation:", recommendation)

thesis = ""

if roe > 0.20:
    thesis += "Strong capital efficiency, "

if roa > 0.10:
    thesis += "Healthy profitability, "

if revenue_cagr > 20:
    thesis += "Exceptional revenue growth, "

if net_income_cagr > 20:
    thesis += "Strong earnings growth, "

if fcf_cagr > 10:
    thesis += "Robust cash flow generation, "

thesis = thesis.rstrip(", ")

print("\nINVESTMENT THESIS")

print("The company demonstrates", thesis)

print("\nDCF VALUATION")

growth_rate = 0.10
discount_rate = 0.12

fcf_year1 = fcf_2026 * (1 + growth_rate)
fcf_year2 = fcf_year1 * (1 + growth_rate)
fcf_year3 = fcf_year2 * (1 + growth_rate)
fcf_year4 = fcf_year3 * (1 + growth_rate)
fcf_year5 = fcf_year4 * (1 + growth_rate)

pv1 = fcf_year1 / ((1 + discount_rate) ** 1)
pv2 = fcf_year2 / ((1 + discount_rate) ** 2)
pv3 = fcf_year3 / ((1 + discount_rate) ** 3)
pv4 = fcf_year4 / ((1 + discount_rate) ** 4)
pv5 = fcf_year5 / ((1 + discount_rate) ** 5)

dcf_value = pv1 + pv2 + pv3 + pv4 + pv5

print("Estimated DCF Value: $", round(dcf_value, 2), "B")

if recommendation in ["STRONG BUY", "BUY"]:
    conclusion = "The company appears fundamentally strong with attractive business characteristics."

elif recommendation == "HOLD":
    conclusion = "The company demonstrates stable fundamentals but requires monitoring."

else:
    conclusion = "The company requires deeper investigation before investment consideration."

market_value = 350

if dcf_value > market_value:
    valuation_status = "UNDERVALUED"

elif dcf_value < market_value:
    valuation_status = "OVERVALUED"

else:
    valuation_status = "FAIRLY VALUED"

print("\nGENERATING PDF REPORT...")
pdf_file = rf"D:\vs code\{company_name}_Research_Report_V25.pdf"

doc = SimpleDocTemplate(pdf_file)

styles = getSampleStyleSheet()

content = []

content.append(
    Paragraph(
        f"{company_name} EQUITY RESEARCH REPORT",
        styles["Title"]
    )
)

content.append(
    Paragraph(
        "Prepared By: Universal Equity Research Platform V25",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        "Prepared For: Educational & Research Purposes",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        " ",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        "EXECUTIVE SUMMARY",
        styles["Heading1"]
    )
)

content.append(
    Paragraph(
        f"Grade: {grade}",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        f"Verdict: {verdict}",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        f"Recommendation: {recommendation}",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        f"DCF Value: ${round(dcf_value,2)} B",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        "FINANCIAL OVERVIEW",
        styles["Heading1"]
    )
)

content.append(
    Paragraph(
        f"Revenue: ${revenue_2026} B",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        f"Net Income: ${net_income_2026} B",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        f"Assets: ${assets_2026} B",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        f"Equity: ${equity_2026} B",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        f"Free Cash Flow: ${fcf_2026} B",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        "BUSINESS QUALITY",
        styles["Heading1"]
    )
)

content.append(
    Paragraph(
        f"ROE: {round(roe * 100,2)}%",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        f"ROA: {round(roa * 100,2)}%",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        f"Business Score: {score}/5",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        "GROWTH ANALYSIS",
        styles["Heading1"]
    )
)

content.append(
    Paragraph(
        f"Revenue CAGR: {round(revenue_cagr,2)}%",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        f"Net Income CAGR: {round(net_income_cagr,2)}%",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        f"Assets CAGR: {round(assets_cagr,2)}%",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        f"Equity CAGR: {round(equity_cagr,2)}%",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        f"FCF CAGR: {round(fcf_cagr,2)}%",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        f"Growth Score: {growth_score}/5",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        "VALUATION ANALYSIS",
        styles["Heading1"]
    )
)

content.append(
    Paragraph(
        f"DCF Value: ${round(dcf_value,2)} B",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        f"Total Score: {total_score}/10",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        f"Grade: {grade}",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        f"Valuation Status: {valuation_status}",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        "REVENUE TREND CHART",
        styles["Heading1"]
    )
)

content.append(
    Image(
        r"D:\vs code\Revenue_Trend.png",
        width=400,
        height=250
    )
)

content.append(
    Paragraph(
        "NET INCOME TREND CHART",
        styles["Heading1"]
    )
)

content.append(
    Image(
        r"D:\vs code\Net_Income_Trend.png",
        width=400,
        height=250
    )
)

content.append(
    Paragraph(
        "FREE CASH FLOW TREND CHART",
        styles["Heading1"]
    )
)

content.append(
    Image(
        r"D:\vs code\FCF_Trend.png",
        width=400,
        height=250
    )
)

content.append(
    Paragraph(
        "PEER COMPARISON CHART",
        styles["Heading1"]
    )
)

content.append(
    Image(
        r"D:\vs code\Peer_Comparison_ROE.png",
        width=400,
        height=250
    )
)

content.append(
    Paragraph(
        "INVESTMENT THESIS",
        styles["Heading1"]
    )
)

content.append(
    Paragraph(
        thesis,
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        "RESEARCH CONCLUSION",
        styles["Heading1"]
    )
)

content.append(
    Paragraph(
        conclusion,
        styles["Normal"]
    )
)

doc.build(content)

print("\nPDF GENERATED SUCCESSFULLY")

print("Saved As:")

print(pdf_file)
