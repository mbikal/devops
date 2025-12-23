import subprocess

def test_pki_output():
    result = subprocess.run(
        ["python3", "pki_tool.py"],
        capture_output=True,
        text=True
    )

    output = result.stdout

    assert "Public key:" in output, "Missing public key"
    assert "Private key:" in output, "Missing private key"

    print("PKI tool test passed!")

if __name__ == "__main__":
    test_pki_output()
