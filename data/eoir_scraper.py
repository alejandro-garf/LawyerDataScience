import re

def load_eoir_pdf(path="data/eoir_pro_bono.pdf"):
    import pytesseract
    from pdf2image import convert_from_path
    import pandas as pd

    print("🧠 Using OCR to extract text from PDF...")
    images = convert_from_path(path)
    all_text = ""

    for i, image in enumerate(images):
        text = pytesseract.image_to_string(image)
        all_text += text + "\n\n"
        print(f"✅ OCR complete for page {i+1}")

    with open("data/raw_eoir_text.txt", "w") as f:
        f.write(all_text)

    # Parse the raw text
    print("🧹 Parsing text into structured rows...")

    entries = []
    blocks = all_text.split("\n\n")
    for block in blocks:
        lines = block.strip().split("\n")
        if len(lines) < 2:
            continue

        name = lines[0].strip()
        organization = lines[1].strip() if len(lines) > 1 else ""
        location = lines[2].strip() if len(lines) > 2 else ""
        state_match = re.search(r"\b[A-Z]{2}\b", location)
        state = state_match.group(0) if state_match else ""

        entries.append({
            "name": name,
            "organization": organization,
            "location": location,
            "state": state,
            "is_pro_bono": True,
            "wage_estimate": None,
            "source": "EOIR"
        })

    df = pd.DataFrame(entries)
    print(f"✅ Parsed {len(df)} lawyer entries.")
    return df
