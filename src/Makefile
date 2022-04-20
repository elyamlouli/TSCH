CONTIKI_PROJECT = coordinator sender node simple-sender
all: $(CONTIKI_PROJECT)

CONTIKI = ../../iot-lab/parts/iot-lab-contiki-ng/contiki-ng

MAKE_MAC = MAKE_MAC_TSCH
MAKE_ROUTING = MAKE_ROUTING_RPL_LITE
MAKE_NET = MAKE_NET_IPV6

MODULES += $(CONTIKI_NG_SERVICES_DIR)/shell
MODULES += $(CONTIKI_NG_SERVICES_DIR)/orhestra

include $(CONTIKI)/Makefile.include
