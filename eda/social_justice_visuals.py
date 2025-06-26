import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    return pd.read_csv("data/parsed_eoir_lawyers.csv")

def lawyers_per_state(df):
    counts = df["state"].value_counts().sort_values(ascending=False)
    plt.figure(figsize=(12, 6))
    counts.plot(kind="bar")
    plt.title("Pro Bono Lawyers per State (EOIR List)")
    plt.xlabel("State")
    plt.ylabel("Number of Lawyers")
    plt.tight_layout()
    plt.savefig("web/static/lawyers_by_state.png")

def org_type_bar(df):
    import matplotlib.pyplot as plt

    def classify_org(org):
        if not isinstance(org, str):
            return "Other"
        org = org.lower()
        if "legal aid" in org:
            return "Legal Aid Org"
        elif "clinic" in org:
            return "Law Clinic"
        elif "center" in org:
            return "Center"
        elif "society" in org:
            return "Society"
        elif "university" in org:
            return "University Program"
        elif "firm" in org:
            return "Private Firm"
        else:
            return "Other"

    df["org_type"] = df["organization"].apply(classify_org)
    counts = df["org_type"].value_counts()

    # Drop "Other"
    counts = counts.drop("Other", errors="ignore")

    plt.figure(figsize=(10, 6))
    bars = counts.sort_values().plot(kind="barh", color="teal", edgecolor="black")

    # Add count labels
    for index, value in enumerate(counts.sort_values()):
        plt.text(value + 1, index, str(value), va='center')

    plt.title("Types of Immigration Legal Service Providers")
    plt.xlabel("Number of Organizations")
    plt.ylabel("Organization Type")
    plt.tight_layout()
    plt.savefig("web/static/org_types.png")
    plt.close()




