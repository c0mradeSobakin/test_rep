def ip_to_int32(ip):
    list_octets = ip.split('.')
    return (int(list_octets[0]) * 16777216) + \
           (int(list_octets[1]) * 65536) + \
           (int(list_octets[2]) * 256) + \
            int(list_octets[3])


ip_to_int32("128.114.17.104")
