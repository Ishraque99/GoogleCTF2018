import fitz

doc = fitz.open("challenge.pdf")

print(doc.loadPage(0).getText("text"))