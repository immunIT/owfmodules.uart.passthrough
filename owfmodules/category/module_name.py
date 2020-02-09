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
        self.options = [
            {"Name": "opt1", "Value": "", "Required": True, "Type": "bool",
             "Description": "opt1 description", "Default": True},
            {"Name": "opt2", "Value": "", "Required": True, "Type": "int",
             "Description": "opt2 description", "Default": ""},
            {"Name": "opt3", "Value": "", "Required": True, "Type": "string",
             "Description": "opt3 description", "Default": "opt3 default value"}
        ]
        # if necessary
        self.advanced_options.append(
            {"Name": "adv_opt_name", "Value": "", "Required": True, "Type": "int",
             "Description": "Advanced option description", "Default": ""}
        )

    def run(self):
        """
        Our code here
        :return:
        """
        # Initialization example
        # Detect and connect to the octowire hardware. Set the self.owf_serial variable if found.
        self.connect()
        if not self.owf_serial:
            return
        try:
            """Call my function here"""
        except (Exception, ValueError) as err:
            self.logger.handle(err, self.logger.ERROR)
