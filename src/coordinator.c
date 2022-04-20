#include "contiki.h"

#include "sys/log.h"
#include "net/routing/routing.h"
#include "net/netstack.h"
#include "net/ipv6/simple-udp.h"
#include <stdio.h>

#define UDP_CLIENT_PORT	8765
#define UDP_SERVER_PORT	5678

/*---------------------------------------------------------------------------*/
PROCESS(coordinator_process, "Coordinator Node");
AUTOSTART_PROCESSES(&coordinator_process);

/*---------------------------------------------------------------------------*/

static struct simple_udp_connection udp_conn;

static void
udp_rx_callback(struct simple_udp_connection *c,
         const uip_ipaddr_t *sender_addr,
         uint16_t sender_port,
         const uip_ipaddr_t *receiver_addr,
         uint16_t receiver_port,
         const uint8_t *data,
         uint16_t datalen)
{
    printf("RX %.*s", datalen, (char*) data);
    printf("\n");
}

PROCESS_THREAD(coordinator_process, ev, data)
{
    PROCESS_BEGIN();

    NETSTACK_ROUTING.root_start();
    NETSTACK_MAC.on();

    simple_udp_register(&udp_conn, UDP_SERVER_PORT, NULL, UDP_CLIENT_PORT, udp_rx_callback);

    PROCESS_END();
}


