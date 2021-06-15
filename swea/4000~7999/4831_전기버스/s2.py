import sys
sys.stdin = open("input.txt", "r")

class ElectricBus:
    def __init__(self, k):
        self.k = k

class BusLine:
    def __init__(self, final_destination, charging_stations):
        self.line = [0] * (final_destination + 1)
        self.charging_stations = charging_stations
        for charging_station in self.charging_stations:
            self.line[charging_station] += 1

    def simulation(self, bus):
        energy = bus.k
        remember_last_charging_station = 0
        cnt = 0
        for now_bus_stop, charging_station in enumerate(self.line[1:-1], start=1):
            energy -= 1
            if charging_station:
                remember_last_charging_station = now_bus_stop

            if not energy:
                if remember_last_charging_station:
                    energy = bus.k - (now_bus_stop - remember_last_charging_station)
                    remember_last_charging_station = 0
                    cnt += 1
                else:
                    return 0

        return cnt

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))

    bus = ElectricBus(K)
    a = BusLine(N, charge)
    aa = a.simulation(bus)
    print(aa)