
1. Write a test for jnpr exercise2.

2. Create a fixture in 'conftest.py' that establishes a PyEZ connection to srx2.
   This fixture should return the PyEZ device object in the 'connected' state.

3. In your test function(s) use the fixture defined in item 2 above.

4. Write a test that tests the 'gather_routes' function. This test should verify the following:

    a. The 'gather_routes' function returns a RouteTable object:
 
        assert isinstance(routes, RouteTable)

    b. The route table returned contains the "0.0.0.0/0" route.

5. Write a test that tests the 'gather_arp_table' function. This test should verify the following:

    a. The 'gather_arp_table' function returns an ArpTable object.

    b. The ARP table returned contains the following MAC address: "00:62:ec:29:70:fe". This is the
       MAC address of the default gateway.
  
