class Solution:
    def defangIPaddr(self, address: str) -> str:
        # Split the IP address string using the dot as a delimiter
        ip_components = address.split(".")

        # Join the components using "[.]"
        formatted_address = "[.]".join(map(str, ip_components))

        # Print the formatted address
        return formatted_address