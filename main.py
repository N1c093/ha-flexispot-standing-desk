import machine
import flexispot

def main():
    f = flexispot.Controlpanel(publish_discovery=False, debug=True)
    for i in range(3):
        f.query_height()

    machine.deepsleep(3 * 60 * 1000)
       
if __name__ == '__main__':
    main()
