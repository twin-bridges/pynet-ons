#import xml.etree.ElementTree as etree
from lxml import etree
import ipdb

ipdb.set_trace()
doc = etree.parse("junos_show_version.xml")
my_xml = doc.getroot()

print(etree.tostring(my_xml, encoding="unicode", pretty_print=True))

junos_version = my_xml.find(".//{*}junos-version")
print(junos_version.text)
