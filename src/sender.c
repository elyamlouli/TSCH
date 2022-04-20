#include "contiki.h"

#include "sys/log.h"
#include "net/routing/routing.h"
#include "net/netstack.h"
#include "net/ipv6/simple-udp.h"
#include "net/ipv6/uip.h"
#include "net/ipv6/uip-ds6-nbr.h"
#include "net/linkaddr.h"

#include "lib/random.h"
#include <stdio.h>

#include "net/net-debug.h"

#include "./define.h"

#ifndef SEED
#define SEED 0
#endif

#ifndef DELAI
#define DELAI 10 * CLOCK_SECOND
#endif

#define UDP_CLIENT_PORT	8765
#define UDP_SERVER_PORT	5678
#define SIZE 64


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
    printf("RX %.*s ", datalen, (char*) data);
    printf("\n");
}


static void 
write_linkaddr_node_addr(char buf[2*LINKADDR_SIZE+1]) {
    unsigned int j;
    for(j = 0; j < LINKADDR_SIZE; ++j) {
        snprintf(buf, 3, "%02x", linkaddr_node_addr.u8[j]);
        buf += 2;
    }
}

/*---------------------------------------------------------------------------*/
PROCESS(sender_process, "Sender Node");
AUTOSTART_PROCESSES(&sender_process);

/*---------------------------------------------------------------------------*/
PROCESS_THREAD(sender_process, ev, data)
{
    static unsigned count;
    static char buf[SIZE];
    static struct etimer periodic_timer;
    static struct etimer delai_timer;
    static char mac_addr[2*LINKADDR_SIZE+1];

    PROCESS_BEGIN();
    NETSTACK_MAC.on();
    random_init(SEED);
    simple_udp_register(&udp_conn, UDP_CLIENT_PORT, NULL, UDP_SERVER_PORT, udp_rx_callback);
    write_linkaddr_node_addr(mac_addr); 

    // wait for serial_aggregator to run
    etimer_set(&delai_timer, CLOCK_SECOND * 3); 
    PROCESS_WAIT_EVENT_UNTIL(etimer_expired(&delai_timer));

    etimer_set(&periodic_timer, DELAI);
    while(1) {
        PROCESS_WAIT_EVENT_UNTIL(etimer_expired(&periodic_timer));

        if(NETSTACK_ROUTING.node_is_reachable()) {
            int i;
            int nb_nodes = uip_ds6_nbr_num();
            unsigned short rand_nb = random_rand() % nb_nodes; 
            uip_ds6_nbr_t * dest = uip_ds6_nbr_head();
            for(i = 1; i < rand_nb; ++i) {
                dest = uip_ds6_nbr_next(dest); 
            }
            snprintf(buf, SIZE, "%s %d", mac_addr, count);
            simple_udp_sendto(&udp_conn, buf, SIZE, &(dest->ipaddr));
            count++;

            printf("TX %s %d\n", mac_addr, count);
        } else {
            printf("ERR Not reachable\n");
        }
        etimer_reset(&periodic_timer);
    }
    PROCESS_END();
}

