from ajazz_controller.core.hid_device import HidDevice

def main() -> None:
    devices = HidDevice.enumerate_all()
    for device in devices:
        vid = device["vendor_id"]
        pid = device["product_id"]
        path = device["path"]
        manufacturer = device.get("manufacturer_string")
        product = device.get("product_string")

        print(f"{vid:04x}:{pid:04x} | {manufacturer} - {product} | {path}")

if __name__ == "__main__":
    main()