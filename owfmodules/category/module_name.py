from octowire_framework.module.AModule import AModule


class ClassName(AModule):
    def __init__(self, owf_config):
        super(ClassName, self).__init__(owf_config)
        self.meta.update({
            'name': '',
            'version': '',
            'description': '',
            'author': ''
        })
        self.options = {
            "opt1": {"Value": "", "Required": True, "Type": "bool",
                     "Description": "opt1 description", "Default": True},
            "opt2": {"Value": "", "Required": True, "Type": "int",
                     "Description": "opt2 description", "Default": ""},
            "opt3": {"Value": "", "Required": True, "Type": "string",
                     "Description": "opt3 description", "Default": "opt3 default value"}
        }
        # if necessary
        self.advanced_options.update({
            "adv_opt_name1": {"Value": "", "Required": True, "Type": "int",
                              "Description": "Advanced option description", "Default": ""},
            "adv_opt_name2": {"Value": "", "Required": True, "Type": "int",
                              "Description": "Advanced option description", "Default": ""}
        })
        # If this module depends of another
        # The syntax of a requirement specifier is defined in full in PEP 508.
        self.dependencies.append(
            "owfmodules.avrisp.my_module>=1.0.0",
            "owfmodules.spi.my_module>=1.0.0"
        )

    def run(self):
        """
        Our code here
        :return:
        """
        # If detect_octowire is True then Detect and connect to the Octowire hardware. Else, connect to the Octowire
        # using the parameters that were configured. It sets the self.owf_serial variable if the hardware is found.
        self.connect()
        if not self.owf_serial:
            return
        try:
            """Call my function here"""
        except (Exception, ValueError) as err:
            self.logger.handle(err, self.logger.ERROR)
