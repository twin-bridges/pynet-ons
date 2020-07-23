Value INTERFACE (\S+)
Value IP_ADDR (\S+)
Value LINE_STATUS ((down|up))
Value LINE_PROTOCOL ((down|up))

Start
  ^Interface.*Protocol$$ -> INT_TABLE

INT_TABLE
  ^${INTERFACE}\s+${IP_ADDR}.*${LINE_STATUS}\s+${LINE_PROTOCOL}\s*$$ -> Record

#Interface                  IP-Address      OK? Method Status                Protocol
#FastEthernet0              unassigned      YES unset  down                  down    
#FastEthernet1              unassigned      YES unset  down                  down    
#FastEthernet2              unassigned      YES unset  down                  down    
#FastEthernet3              unassigned      YES unset  down                  down    
#FastEthernet4              10.220.88.20    YES NVRAM  up                    up      
#Vlan1                      unassigned      YES unset  down                  down    

