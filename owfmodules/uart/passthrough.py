from octowire_framework.module.AModule import AModule
from octowire.utils.serial_utils import detect_octowire
from octowire.uart import UART
from octowire_framework.core.commands.miniterm import miniterm


class ClassName(AModule):
    def __init__(self, owf_config):
        super(ClassName, self).__init__(owf_config)
        self.meta.update({
            'name': 'miniterm UART passthrough',
            'version': '1.0.0',
            'description': 'Enter the Octowire UART passthrough and then open a miniterm session',
            'author': 'Jordan Ovrè / Ghecko <jovre@immunit.ch>, Paul Duncan / Eresse <pduncan@immunit.ch>'
        })
        self.options = {
            "uart_interface": {"Value": "", "Required": True, "Type": "int",
                               "Description": "The Octowire UART interface (0=UART0 or 1=UART1)", "Default": 0},
            "baudrate": {"Value": "", "Required": True, "Type": "int",
                         "Description": "The baudrate value to communicate with the target",
                         "Default": 9600},
        }
        self.uart_instance = None

    def uart_pt_miniterm(self):
        """
        Open a miniterm session, with the Octowire in the UART passthrough mode
        if a valid baudrate value is found and the user select 'yes' when asked.
        :return: Nothing.
        """
        # Set and configure UART interface
        self.uart_instance = UART(serial_instance=self.owf_serial, interface_id=self.options["uart_interface"]["Value"])
        self.uart_instance.configure(baudrate=self.options["baudrate"]["Value"])

        # Enter UART passthrough
        self.uart_instance.passthrough()

        # Close the actual octowire serial instance
        self.owf_serial.close()
        if self.config["OCTOWIRE"]["detect"]:
            octowire_port = detect_octowire(verbose=False)
            self.config['OCTOWIRE']['port'] = octowire_port

        # Open a miniterm session
        miniterm(None, self.config)
        self.logger.handle("Please press the Octowire User button to exit the UART "
                           "passthrough mode", self.logger.USER_INTERACT)

    def run(self):
        """
        Main function.
        Enter UART passthrough an open a miniterm session.
        :return:
        """
        # If detect_octowire is True then Detect and connect to the Octowire hardware. Else, connect to the Octowire
        # using the parameters that were configured. It sets the self.owf_serial variable if the hardware is found.
        self.connect()
        if not self.owf_serial:
            return
        try:
            self.uart_pt_miniterm()
        except ValueError as err:
            self.logger.handle(err, self.logger.ERROR)
        except Exception as err:
            self.logger.handle("{}: {}".format(type(err).__name__, err), self.logger.ERROR)
