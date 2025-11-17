def main() -> None:
    username = input("What is your name?")
    print(f"Hello {username}!")
    
def cel_to_fahr(c : float) -> float:
    return c * 9/5 + 32

if __name__ == "__main__":
    main()