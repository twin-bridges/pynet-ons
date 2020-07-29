Value INTERFACE (\S+)
Value IP_ADDR (xxx\S+)
#Value LINE_STATUS ((upx|downx))
#Value LINE_PROTOCOL ((upx|downx))

Start
  ^Interface.*Protocol$$ -> Show_ip

Show_ip
  ^${INTERFACE}.*$$ -> Record
#  ^${INTERFACE}\s+${IP_ADDR}.*$$ -> Record
#  ^${INTERFACE}\s+${IP_ADDR}.+${LINE_STATUS}\s+${LINE_PROTOCOL}.*$$ -> Record

#Interface                  IP-Address      OK? Method Status                Protocol
#FastEthernet0              unassigned      YES unset  down                  down    
#FastEthernet1              unassigned      YES unset  down                  down    
#FastEthernet2              unassigned      YES unset  down                  down    
#FastEthernet3              unassigned      YES unset  down                  down    
#FastEthernet4              10.220.88.20    YES NVRAM  up                    up      
#Vlan1                      unassigned      YES unset  down                  down    

