from fpdf import FPDF

def main():
    name = input("Name: ").strip().title()
    create_pdf(name)

def create_pdf(name):
    pdf = FPDF(orientation="P", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", "B", 38)
    pdf.cell(w=0, h=50, txt="CS50 Shirtificate", align="C")
    pdf.set_xy(0,65)
    pdf.image("shirtificate.png", x="C", w=pdf.epw)
    pdf.set_font("helvetica", size=24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_y(120)
    pdf.cell(0,None,f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()


