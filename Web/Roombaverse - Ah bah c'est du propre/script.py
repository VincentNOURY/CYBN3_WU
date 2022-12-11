import uuid
import datetime

global _last_timestamp
import time
timestamp = 138900061685840894
# time uuid trouvé sur la page communauté
_last_timestamp = timestamp
clock_seq = 2173
# Clock trouvé en décodant l'uuid de mon compte
time_low = timestamp & 0xffffffff
time_mid = (timestamp >> 32) & 0xffff
time_hi_version = (timestamp >> 48) & 0x0fff
clock_seq_low = clock_seq & 0xff
clock_seq_hi_variant = (clock_seq >> 8) & 0x3f
node = 2482558207860
# Trouvé depuis l'uuid de mon compte (puis convertit)
print(uuid.UUID(fields=(time_low, time_mid, time_hi_version, clock_seq_hi_variant, clock_seq_low, node), version=1))
