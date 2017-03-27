import _winreg

keyName = "myKey"


def write_to_registry():
    try:
        key = _winreg.CreateKey(_winreg.HKEY_CURRENT_USER, "Software\\" + keyName)
        _winreg.SetValueEx(key, "myVal", 0, _winreg.REG_SZ, "This is a value.")
        print("value created")
    except Exception as e:
        print(e)


def read_from_registry():
    try:
        with _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, "Software\\" + keyName, 0, _winreg.KEY_READ) as key:
            if key:
                data = _winreg.QueryValueEx(key, "myVal")
                print("Read from registry: ", data)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    write_to_registry()
    read_from_registry()
