Value INTERFACE (\S+)
Value IP_ADDR (\S+)
Value LINE_STATUS ((up|down))
Value LINE_PROTOCOL ((up|down))

Start
  ^Interface.*Protocol$$ -> Show_ip

Show_ip
  ^${INTERFACE}\s+${IP_ADDR}.+${LINE_STATUS}\s+${LINE_PROTOCOL}.*$$ -> Record

#Interface                  IP-Address      OK? Method Status                Protocol
#FastEthernet0              unassigned      YES unset  down                  down    
#FastEthernet1              unassigned      YES unset  down                  down    
#FastEthernet2              unassigned      YES unset  down                  down    
#FastEthernet3              unassigned      YES unset  down                  down    
#FastEthernet4              10.220.88.20    YES NVRAM  up                    up      
#Vlan1                      unassigned      YES unset  down                  down    

