from ajazz_controller.core.ajazz_device import AjazzDevice

def main():
    device = AjazzDevice()
    device.open()
    
    print("Setting brightness to 50%...")
    device.set_brightness(50)
    
    device.close()
    print("Done!")

if __name__ == "__main__":
    main()
