
class Person():

    def __init__(self, firstName, lastName, phoneNumber, dateOfBirth):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.dateOfBirth = dateOfBirth
        self.addresses = []

    def add_address(self, address):
        from address import Address
        if isinstance(address,Address):
            self.addresses.append(address)
        elif isinstance(address, list):
            for entry in address:
                if not isinstance(entry, Address):
                    raise Error('Invalid Address.')
            self.addresses = address
        else:
            raise Error('Invalid Address.')


    def convert_addresses_into_string(self):
        if len(self.addresses) != 0:
            str_addresses = ''
            counter = 0
            for address in self.addresses:
                str_ = address.country + ' ' + address.city + ' ' + address.street + ' ' + address.postal + ';'
                str_addresses += str_
                counter +1

            return str_addresses
