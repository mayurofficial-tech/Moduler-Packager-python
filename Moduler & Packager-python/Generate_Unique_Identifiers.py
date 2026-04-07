import uuid


def unique_identifier():
    print("=" * 30)
    print("Generate uuid:-",uuid.uuid4())
    print("=" * 30)
def main():
    print("Generating Unique Identifiers:")
    unique_identifier()

if __name__ == "__main__":
    main()