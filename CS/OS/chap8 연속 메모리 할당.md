## chap8 메모리 관리 (연속 할당)

[toc]

### 1. 메모리 배경지식

1. 메모리(기억장치)의 종류

   - (저용량, 고속, 비쌈) 레지스터 - 캐시 - 메인 메모리 - 보조기억장치 (고용량, 저속, 저렴)
     - HW(CPU)가 관리 : 레지스터, 캐시
     - SW(OS)가 관리 : 메인 메모리, 보조기억장치
   - 나눠지게 된 원인 : I/O bottleneck (병목현상)을 해소하기 위해

   <br/>

2. 메모리(기억장치)의 계층구조

   <img src="chap8 연속 메모리 할당.assets/image-20210829041317427.png" alt="image-20210829041317427" style="zoom:67%;" />

   - Block : 보조기억장치와 주기억장치 사이의 데이터 전송 단위. Size: 1~4KB
   - Word : 주기억장치와 레지스터 사이의 데이터 전송 단위. Size: 16~64bits
     - CPU에서 32bit, 64bit의 기준이 Word. Word의 크기만큼 데이터를 한 번에 읽어온다.

   <br/>

3. Address Binding

   - 프로그램의 논리 주소를 실제 메모리의 물리 주소로 매핑(mapping)하는 작업

   - Binding 시점에 따른 구분

     - Compile time binding
       - 프로세스가 메모리에 적재될 위치를 컴파일러가 알 수 있는 경우. **위치가 변하지 않음**
       - 프로그램 전체가 메모리에 올라가야 함
     - Load time binding
       - 메모리 적재 위치를 컴파일 시점에서 모르면, 대체 가능한 **상대주소를 생성**
       - 적재 시점(load time)에 시작주소를 반영하여 사용자 코드 상의 주소를 재설정
       - 프로그램 전체가 메모리에 올라가야 함
     - Run time binding
       - Address binding을 수행시간까지 연기 (ready → running 상태가 될 때 address 정의)
       - 프로세스가 수행 도중 다른 메모리 위치로 이동할 수 있음.
       - HW의 도움이 필요 : MMU (Memory Management Unit)
       - 대부분의 OS가 사용

     <img src="chap8 연속 메모리 할당.assets/image-20210829040513784.png" alt="image-20210829040513784" style="zoom: 67%;" />

   <br/>

4. Dynamic Loading

   - 모든 루틴(function)을 교체 가능한 형태로 디스크에 저장
   - **실제 호출 전까지는** 루틴을 적재하지 않음
     - 메인 프로그램만 메모리에 적재하여 수행
     - 루틴의 호출 시점에 address binding 수행
   - 장점 : 메모리 공간의 효율적 사용

   <br/>

5. Swapping

   - 프로세서 할당이 끝나고 수행 완료도니 프로세스는 swap-device로 보내고 (Swap-out)
   - 새롭게 시작하는 프로세스는 메모리에 적재 (Swap-in)

<br/>

<br/>

<br/>


### 2. Continuous Memory Allocation (메모리 연속 할당)

1. Continuous Memory Allocation (연속 할당)

   - 프로세스 (context) 를 하나의 연속된 메모리 공간에 할당. 프로그램, 데이터, 스택 등
   - 메모리 구성 정책
     - 메모리에 동시에 올라갈 수 있는 **프로세스의 수**
     - 각 프로세스에게 할당되는 **메모리 공간 크기**
     - 메모리 **분할 방법**

   <br/>

2. Uni-programming

   - **하나의 프로세스만** 메모리 상에 존재
   - 문제점 : 프로그램의 크기 > 메모리의 크기 일 때
     - 해결법 : Overlay structure
       - 메모리에 현재 필요한 영역만 적재
       - 사용자가 프로그램의 흐름 및 자료구조를 모두 알고 있어야 함
   - 문제점 : 커널 (Kernel) 보호
     - 해결법 : 경계 레지스터 (boundary register) 사용
   - 문제점 : Low system resource utilization (메모리 공간 낭비), Low system performance
     - 해결법 : Multi-programming

   <br/>

3. Fixed Partition Multi-programming (FPM) 

   - 메모리 공간을 **고정된 크기로 미리 분할**하는 방법
   - 한 프로세스는 한 partition에 적재한다 : partition의 수 = K = Multiprogramming degree
   - 장) 메모리 관리가 간편. Low overhead
   - 단) Fragmentation (단편화) 발생
     - Internal fragmentation (내부 단편화) : partition 크기 > process 크기 (메모리 낭비)
     - External fragmentation (외부 단편화) : 남은 메모리 크기 > process 크기지만, 연속된 공간 X (메모리 낭비)

   <br/>

4. Variable Partition Multiprogramming (VPM)

   - 초기에는 전체가 하나의 영역. 후에 **프로세스 처리 과정**에서 메모리 공간을 **동적 분할**

   - External fragmentation (외부 단편화) 발생

     - Internal fragmentation (내부 단편화) : 프로세스 적재할 때마다 할당하므로 **발생 X**

     - 해결법1 - Coalescing holes (공간 통합) : process가 memory를 release하고 나가면, **인접한 빈 영역을 하나의 partiton으로 통합** 해서 process를 할당한다. 낮은 오버헤드

       <img src="chap8 연속 메모리 할당.assets/image-20210829044936640.png" alt="image-20210829044936640" style="zoom:67%;" />

     - 해결법2 - Storage Compaction (메모리 압축) : 실행하고 있는 process를 모두 중지하고, **memory를 재배치해서 빈 공간을 하나로 통합**한다. 높은 오버헤드, 많은 시스템 자원 소비

       <img src="chap8 연속 메모리 할당.assets/image-20210829044955829.png" alt="image-20210829044955829" style="zoom:67%;" />

   - 배치 전략 (Placement strategies)

     - Frist-fit(최초 적합) : 충분한 크기를 가진 **첫번째 partition**을 선택
       - 장) 간단. 낮은 오버헤드. 단) **공간 활용률**이 떨어질 수 있음
     - Best-fit(최적 적합) : process가 들어갈 수 있는 partition 중 **가장 작은 곳** 선택
       - 모든 partition을 살펴봐야해서 오래 걸림 (높은 오버헤드) 
       - 장) 크기가 큰 partiton을 유지 가능. 단) 활용하기 힘든 작은 크기의 partition이 많이 발생
     - Worst-fit(최악 적합) : process가 들어갈 수 있는 partiton 중 **가장 큰 곳** 선택
       - 모든 partition을 살펴봐야해서 오래 걸림 (높은 오버헤드) 
       - 장) 작은 크기의 partition 발생을 줄임. 단) 큰 크기의 partition 확보가 어려움
     - Next-fit(순차 최초 적합) : State table에서 마지막으로 탐색한 위치부터 탐색하는 최초 적합
       - 장) 메모리 영역의 사용 빈도 균등화. 낮은 오버헤드