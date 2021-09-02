## chap10 가상 메모리 관리

[toc]

### 1. Virtual Memory Manangement

1. 가상 메모리 (기억 장치)
   - Non-continuous allocation : 사용자 프로그램을 block 단위로 분할하여 적재/실행
   - Paging/Segmentation system
   - 관리 목적 : 성능 최적화 (Cost model)
2. Cost model (Page sys)
   - Page fault frequency (발생 빈도) & Page fault rate (발생률) => 오버헤드에 비례
     - Page fault : swap device에서 해당 page를 메모리에 적재해두지 않은 경우
     - Page fault rate를 최소화 해야한다. 
   - Page reference string (d) : 프로세스의 수행 중 **참조한 페이지 번호 순서**
     - w = r1 · r2 · r3 ... rk (페이지 번호 1, 2, ... k)
   - Page fault rate F(w) : **전체 참조한 페이지 중에 몇 번 page fault가 발생**했는지
     - F(w) = Num of page faults during w / |w|
     - |w| : 프로세스가 실행하면서 참조한 페이지의 수 

<br/>

<br/>

### 2. Hardware components

1. Hardware Components

   - Address translation device (주소 사상 장치) : **주소 사상을 효율적**으로 수행하기 위해 (TLB 등)
   - Bit Vectors : **Page 사용 상황**에 대한 정보를 기록하는 비트들
     - 페이지 프레임의 페이지를 바꿔야할 때, 어떤 기준으로 바꿀지 정보를 제공
     - 페이지 프레임 (pf)마다 refenece/update bits가 하나씩 있다.

2. Bit Vectors

   - Refrenece bits (used bit) : 참조 비트 
     - 메모리에 적재된 각각의 page가 **최근에 참조**되었는지를 표시
     - 프로세스에 의해 참조되면 해당 page의 Ref.bit를 1로 설정 & 주기적으로 0으로 변경
   - Update bits (modified bits, write bits, **dirty bits**) : 갱신 비트
     - Page가 메모리에 적재된 후, 프로세스에 의해 **수정되었는지**를 표시
     - 프로세스에 의해 page가 수정되면, 해당 page의 (main memory 상 내용) != (Swap device의 내용)이 된다. 때문에 메모리에서 page가 나올 때 해당 page에 대한 **Write-back (to swap device)**이 필요하다. 이러한 이유로 Update bits가 필요하다.
     - 주기적 초기화 X => 메모리에서 나올 때 초기화

   <img src="chap10 가상 메모리 관리.assets/image-20210903022653222.png" alt="image-20210903022653222" style="zoom:67%;" />

<br/>

<br/>

### 2. Software components

1. 가상 메모리 성능 향상을 위한 관리 기법들
2. Allocation strategies (할당 기법) : 각 프로세스에게 메모리를 **얼마만큼 줄 것**인가?
   - Fixed allocation (고정 할당) : 프로세스의 실행동안 **고정된 크기의 메모리 할당**
   - Variable allocation (가변 할당) : 프로세스의 실행동안 할당하는 메모리 크기가 **유동적**
   - 고려사항 : 프로세스 실행에 필요한 **메모리 양을 예측**해야 함
     - 너무 큰 메모리 할당 : 메모리 낭비
     - 너무 작은 메모리 할당 : Page fault rate 증가, 시스템 성능 저하
3. Fetch Strategies : 특정 page를 메모리에 **언제 적재**할 것인가?
   - Demand fetch (demand paging) : **필요할 때** 적재. 프로세스가 참조하는 페이지들만 적재
     - page fault overhead 존재
     - 실제 대부분의 시스템. 준수한 성능.
   - Anticipatory fetch (pre-paging) : 가까운 미래에 **참조될 가능성**이 높은 page 예측
     - 예측 성공시 page fault overhead 없음. 잘못된 예측 시 자원 낭비 큼
     - prediction overhead (예측해야하는 오버헤드, kernel의 개입), hit ratio에 민감
4. Placement Strategies : page/segment를 **어디에 적재**할 것인가?
   - Paging system에는 불필요 (공간의 크기가 일정해서)
   - Segmentation system에서의 배치 기법
     - First-fit / Best-fit / Worst-fit / Next-fit
5. **Replacement Strategies** : **새로운 page를 어떤 page와 교체**할 것인가? (빈 page frame이 없는 경우)
   - Fixed allocation을 위한 교체 기법
     - MIN(OPT, B0) algorithm
     - Random algorithm
     - FIFO(First In First Out) algorithm
     - LRU(Least Recently Used) algorithm
     - LFU(Least Frequently Used) algorithm
     - NUR(Not Used Recently) algorithm
     - Clock algorithm
     - Second chance algorithm
   - Variable allocation을 위한 교체 기법
     - VMIN(Variable MIN) algorithm
     - WS(Working Set) algorithm
     - PFF(Page Fault Frequency) algorithm
6. Cleaning Strategies : **변경된 page를 언제 write-back** 할 것인가?
   - Demand cleaning : 해당 page에 메모리에서 내려올 때 write-back . 대부분의 시스템
   - Anticipatory cleaning (pre-cleaning) : 더이상 변경될 가능성이 없다고 판단될 때 미리 write-back
     - 예측 성공시 page 교체시 발생하는 write-back 시간 절약
     - 예측 실패시 자원 낭비가 크다. + prediction overhead (예측하는데에 오버헤드)
7. Load Control Strategies : 시스템의 **multi-prograaming degree 조절** 
   - 적정 수준의 multi-programming degree를 유지 해야함
     - 저부하 상태 : 시스템 자원 낭비, 성능 저하
     - 고부하 상태 : 자원에 대한 경쟁 심화, 성능 저하, **Thrashing (과도한 page fault) 현상 발생**

<br/>

<br/>

### 3. Page replacement schemes



