# alternate_merge.py
# Quick • Unique • Easy Program: Alternate Merge of Two Strings

def alternate_merge(s1, s2):
    merged = ""
    length = max(len(s1), len(s2))

    for i in range(length):
        if i < len(s1):
            merged += s1[i]
        if i < len(s2):
            merged += s2[i]

    return merged


if __name__ == "__main__":
    print("🔀 Alternate Merge of Two Strings")
    print("--------------------------------")

    a = input("Enter first string: ")
    b = input("Enter second string: ")

    print("\nMerged Output:")
    print(alternate_merge(a, b))
