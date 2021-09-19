# chap12 입출력 시스템 & 디스크 관리

## I/O Mechanisms

1. I/O System (HW)

2. Processor controlled memory access

   <img src="chap 12 입출력 시스템 & 디스크 관리.assets/image-20210920012731494.png" alt="image-20210920012731494" style="zoom:80%;" />

   - Polling (Programmed I/O)
     - Process가 계속 동작하며 **주기적으로 I/O 장치의 상태 확인** 
     - 장점 : 간단. I/O 장치가 빠르고 데이터 전송이 잦은 경우 효율적
     - 단점 : Processor의 부담이 큼. Polling overhead
   - Interrupt
     - I/O 장치가 작업을 완료한 후, **자신의 상태를 Processor에게 전달**
     - 장점 : Pooling 대비 low overhead. 불규칙적인 요청 처리에 적합
     - 단점 : interrupt handling overhead

3. Direct Memory Access (DMA)

   - Processor controlled memory access은 Processor가 모든 데이터 전송을 처리해야한다는 문제가 있다
     - 따라서 DMA를 활용할 수 있음
   - DMA : I/O 장치와 Memory 사이의 데이터 전송을 Processor 개입 없이 수행 (메모리, I/O 직접 연결)
     - Processor는 데이터의 전송 시작/종료만 관여

   <img src="chap 12 입출력 시스템 & 디스크 관리.assets/image-20210920012708011.png" alt="image-20210920012708011" style="zoom:67%;" />

<br/>

## I/O services of OS

1. I/O Scheduling

   - 입출력 요청에 대한 처리 순서 결정
     - 시스템의 전반적 성능 향상, Process 의 요구에 대한 공평한 처리
   - disk I/O scheduling

2. Error handling

   - 입출력 중 발생하는 오류 처리
   - disk access fail, network communication error 등

3. I/O device information mangements

4. Buffering

   - I/O 장치와 Program 사이에 전송되는 데이터를 **Buffer에 임시 저장**
   - 전송 속도 (or 처리 단위) 차이 문제 해결

   <img src="chap 12 입출력 시스템 & 디스크 관리.assets/image-20210920013450019.png" alt="image-20210920013450019" style="zoom:67%;" />

5. Caching

   - **자주 사용하는 데이터를 미리 복사**해 둠. Cache hit 시, I/O 생략 가능

6. Spooling

   - 한 I/O 장치에 여러 Program이 요청을 보낼 시, **출력이 섞이지 않도록** 하는 기법
     - 각 Program에 대응하는 disk file에 기록 (spooling)
     - spooling이 완료되면, spool을 한 번에 하나씩 I/O 장치로 전송

<br/>

## Disk Scheduling

1. Disk Scheduling

   - Disk access 요청들의 처리 순서를 결정하고, 성능을 향상시키기 위해
   - 평가 기준 : Throughput, Mean response time, Predictability (응답 시간이 예측 가능한가)
   - Data access time = Seek time + Rotational delay + Data transmission time
     - 최적화 할 수 있는 건 Seek time, Rotational delay

2. Optimizing **Seek time**

   - Frist Come First Service (FCFS)

     - 요청이 **도착한 순서에 따라** 처리. Disk access 부하가 적은 경우에 적합
     - 장점 : 간단. 공평한 처리 기법 (무한 대기 방지)
     - 단점 : 최적 성능 달성에 대한 고려 X

     <img src="chap 12 입출력 시스템 & 디스크 관리.assets/image-20210920015321152.png" alt="image-20210920015321152" style="zoom:67%;" />

   - Shortest Seek Time First (SSTF)

     - 현재 head 위치에서 **가장 가까운 요청 먼저** 처리. 일괄 처리 시스템에 적합
     - 장점 : Throughput 증가, 평균 응답 시간 감소
     - 단점 : Predictability 감소, **Starvation 현상** 발생 가능

   - Scan Scheduling

     - 현재 head의 **진행 방향에서 head와 가장 가까운 요청 먼저** 처리하고, **마지막 cylinder 도착한 후, 반대** 방향으로 진행
     - 장점 : Throughput 증가, 평균 응답 시간 감소, SSTF의 **starvation 문제 해결**
     - 단점 : 진행 방향 반대쪽 끝의 요청들의 응답시간 증가

     <img src="chap 12 입출력 시스템 & 디스크 관리.assets/image-20210920015725266.png" alt="image-20210920015725266" style="zoom:67%;" />

   - C-Scan Scheduling

     - Scan과 유사. Head가 미리 **정해진 방향으로만** 이동. 마지막 cylinder 도착 후 시작 cylinder로 이동
     - 장점 : Scan 대비 균등한 기회 제공

   - Look Scheduling

     - **Elevator** algorithm. Scan(C-Scan)에서 **현재 진행 방향에 요청이 없으면 방향 전환**. 마지막 cylinder까지 이동 X. Scan(C-Scan)의 실제 구현
     - 장점 : Scan의 불필요한 head 이동 제거

3. Optimizing **Rotational Delay**

   - Shortest Latency Time First (SLTF)
     - Fixed head disk 시스템의 경우, Sector queuing algorithm을 사용
       - 각 sector 별 queue 유지. head 아래 도착한 sector의 queue에 있는 요청을 먼저 처리
     -  Moving head disk 시스템의 경우
       - 같은 cylinder에 여러개의 요청 처리를 위해 사용 가능
       - Head가 특정 cylinder에 도착하면, 고정 후 해당 cylinder의 요청을 모두 처리
   - Shortest Positioning Time First (SPTF)
     - Positioning time = Seek time + rotational delay 이 가장 작은 요청 먼저 처리
     - 장점 : Throughput 증가, 평균 응답 시간 감소
     - 단점 : 가장 안쪽과 바깥쪽 cylinder 의 요청에 대해 **starvation 현상** 발생 가능
       - Eschenbash scheduling : Positioning time을 최적화 시도
       - Disk가 1회전 하는 동안 요청을 처리할 수 있도록 요청을 정렬

<br/>

## RAID Architecture

1. Redundant Array of Inexpensive Disks (RAID)

   - 여러 개의 물리 disk를 하나의 논리 disk로 사용 (OS support, RAID controller)
   - Disk system의 성능 향상을 위해 사용 (접근 속도, 신뢰성)

2. RAID 0 (성능 중심)

   - Disk striping : 논리적인 한 block을 **일정한 크기로 나누어 각 disk에 나누어** 저장
   - 장점 : 모든 disk에 입출력 부하 균등 분배 => 병렬적으로 접근 => **속도 향상**
   - 단점 : 한 disk에서 **장애 시, 데이터 손실** 발생 => Low reliability

   <img src="chap 12 입출력 시스템 & 디스크 관리.assets/image-20210920022415589.png" alt="image-20210920022415589" style="zoom:67%;" />

3. RAID 1 (안전 중심)

   - Disk mirroring : 동일한 데이터를 **mirroring disk에 중복 저장**. 최소 2개의 disk로 구성
   - 장점 : 한 disk에 장애가 생겨도 데이터 손실
   - 단점 : 가용 disk의 용량 = 전체 disk 용량 / 2

   <img src="chap 12 입출력 시스템 & 디스크 관리.assets/image-20210920022427217.png" alt="image-20210920022427217" style="zoom:67%;" />

4. RAID 3

   - RAID 0 + parity disk
     - **Byte 단위 분할** 저장. 모든 disk에 입출력 부하 균등 분배
   - 장점 : 한 disk에 장애 발생시, parity 정보를 이용하여 복구
   - 단점 : Write 시 parity 계산 필요 => overhead, wirte가 몰릴 시, 병목 현상 발생 가능

   <img src="chap 12 입출력 시스템 & 디스크 관리.assets/image-20210920022439090.png" alt="image-20210920022439090" style="zoom: 80%;" />

5. RAID 4

   - RAID 3와 유사. 단 **Block 단위로 분산** 저장
     - 독립적으로 access 가능. Disk간 균등 분배가 안될 수 있음
   - 장점 : 한 disk에 장애 발생시, parity 정보를 이용하여 복구
   - 단점 : Write 시 parity 계산 필요 => overhead, wirte가 몰릴 시, 병목 현상 발생 가능\

   <img src="chap 12 입출력 시스템 & 디스크 관리.assets/image-20210920022803729.png" alt="image-20210920022803729" style="zoom:80%;" />

6. RAID 5

   - RAID 4와 유사(독립적으로 access) Parity 정보를 각 disk에 분산 저장
     - Parity disk의 병목 현상 문제 해소
     - 현재 가장 널리 사용되는 RAID level 중 하나

   <img src="chap 12 입출력 시스템 & 디스크 관리.assets/image-20210920022750904.png" alt="image-20210920022750904" style="zoom:80%;" />

