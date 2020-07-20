from lxml import etree

# import xml.etree.ElementTree as etree
import ipdb

# This will be an ElementTree
doc = etree.parse("show_ver1.xml")

ipdb.set_trace()
print(doc)
print(doc.getroot())

# This will be an Element
my_tree = doc.getroot()

# Look at the XML as a string (must decode as byte-string)
print(etree.tostring(my_tree, encoding="unicode", pretty_print=True))
print(my_tree)

# Loop over the children of the tree
for e in my_tree:
    print(e)

children = my_tree.getchildren()

xml_string = """
<rpc-reply xmlns:junos="http://xml.juniper.net/junos/12.1X44/junos">
     <software-information>
         <host-name>pynet-jnpr-srx1</host-name>
         <product-model>srx100h2</product-model>
         <product-name>srx100h2</product-name>
         <jsr/>
         <package-information>
             <name>junos</name>
             <comment>JUNOS Software Release [12.1X44-D35.5]</comment>
         </package-information>
     </software-information>
     <cli>
         <banner/>
     </cli>
</rpc-reply>
"""

new_tree = etree.fromstring(xml_string)
print(new_tree)

host_name = my_tree.find(".//host-name")
product_model = my_tree.find(".//product-model")

comment = ipdb > my_tree.find("./package-information/comment").text
