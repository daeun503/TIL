## chap7 교착상태

[toc]

### 1. Deadlock 의 개념

1. Deadlock vs Blocked/Asleep

   - Deadlock state
     - 프로세스가 **발생 가능성이 없는 이벤트**를 기다리는 경우
     - asleep 상태에 존재 (자원/이벤트를 기다리는데 일어날 가능성이 X)
   - Blocked/Asleep state
     - 프로세스가 특정 이벤트를 기다리는 상태
     - 프로세스가 필요한 자원을 기다리는 상태

   <br/>

2. Deadlock vs Starvation 

   - Deadlock
     - **Asleep** 상태에 존재
     - **자원/이벤트**를 기다리는데  **발생 가능성이 없음**
   - Starvation
     - **Ready** 상태에 존재
     - **CPU**를 기다리는 중인데 우선순위가 낮아서 할당 못 받는 중. **발생 가능성이 있긴 함**

   <img src="chap7 교착상태.assets/image-20210822163422081.png" alt="image-20210822163422081" style="zoom:67%;" />

   <br/>

3. 자원의 분류

   - 일반적 분류 : 하드웨어 자원 vs 소프트웨어 자원
   - 선점 가능 여부에 따른 분류
     - Preemptible resources : 선점 당한 후, **돌아와도 문제가 발생하지 않는** 자원. 프로세서, 메모리 등
     - **Non-preemptible resources** : 선점 당하면, 이후 진행에 **문제가 발생**하는 자원. Rollback, restart 등 특별한 동작이 필요. disk drive 등
   - 할당 단위에 따른 분류
     - Total allocation resources : **자원 전체를 프로세스에게 할당**. 프로세서, disk drive 등
     - Partitioned allocation resources : 하나의 자원을 **여러 조각**으로 나누어, 여러 프로세스들에게 할당. 메모리 등
   - 동시 사용 가능 여부에 따른 분류
     - **Exclusive allocation resources** : **한 순간에 한 프로세스만** 사용 가능한 자원. 프로세서, 메모리, disk drive 등
     - Shared allocation resource : **여러 프로세스가 동시에** 사용 가능한 자원. 프로그램(sw), shared data 등
   - 재사용 가능 여부에 따른 분류
     - **SR (Serially-reuable Resources)** : 시스템 내에 **항상 존재**하는 자원. 사용이 끝나면 다른 프로세스가 **재사용** 가능. 프로세서, 메모리, disk drive, program 등
     - CR (Consumable Resources) : 한 프로세스가 **사용한 후에 사라지는** 자원. signal, message 등

   <br/>

4. Deadlock과 자원의 종류

   - **Deadlock을 발생시킬 수 있는 자원의 형태** (할당 단위는 영향X)
     - Non-preemptible resources
     - Exclusive allocation resources
     - SR (Serially-reuable Resources)
   - CR (Consumable Resources) 을 대상으로 하는 Deadlock model은 너무 복잡 => 고려 X

<br/>

<br/>

<br/>

### 2. Deadlock model (표현법)

1. Graph Model

   - 구성 

     - Node : 프로세스 노드 P1, P2와 자원노드 R1, R2
     - Edge : Rj -> Pi : 자원이 프로세스에 할당됨 & Pi -> Rj : 프로세스가 자원을 요청

     <img src="chap7 교착상태.assets/image-20210822171321661.png" alt="image-20210822171321661" style="zoom:67%;" />

   <br/>

2. State Transition Model

   - 예제

     - 2개의 프로세스와 A type의 자원 2개 존재
     - 프로세스는 한 번에 자원 하나만 요청/반납 가능

   - State 

     - 프로세스가 1개 이면 아래와 같이 5개의 state가 만들어진다.
     - 프로세스가 2개이면 5x5개의 state가 만들어진다.

     <img src="chap7 교착상태.assets/image-20210822171109823.png" alt="image-20210822171109823" style="zoom:67%;" />

   - State Transition Model로 확장 (프로세스 2개)

     - 빨간 S33에서 데드락 발생
     - S32, S23에서 S33으로 이동하는 것을 막아서 데드락 해결 가능

     <img src="chap7 교착상태.assets/image-20210822171237178.png" alt="image-20210822171237178" style="zoom:80%;" />

   <br/>

3. **Deadlock 발생 필요 조건 4가지**

   - 자원의 특성
     - Exclusive use of resources
     - Non-preemptible resources
   - 프로세스의 특성
     - Hold and wait (Partial allocation) : 자원을 하나 hold하고 다른 자원 요청
     - Circular wait

<br/>

<br/>

<br/>

### 3. Deadlock 해결 방법들

1. Deadlock 예방법 : 4개의 deadlock 발생 필요 조건 중 하나를 제거

   - Exclusive use of resources 조건 제거
     - 모든 자원을 공유 허용 : 현실적으로 불가능
   - Non-preemptible resources 조건 제거
     - 모든 자원에 대해 선점 허용 : 현실적으로 불가능
     - 유사한 방법 : 프로세스가 할당 받을 수 없는 자원을 요청한 경우, 기존에 가지고 있던 자원을 모두 반납하고 작업 취소 (이후 처음부터 다시 시작) => 심각한 자원 낭비 발생 => 비현실적
   - Hold and wait (Partial allocation) 조건 제거
     - 필요 자원 모두 한번에 모두 할당 (Total allocation) : 가능은 하지만 비효율적
     - 필요하지 않은 순간에도 자원을 가지고 있음 => 자원 낭비 발생 & 무한 대기 현상 발생 가능
   - Circular wait 조건 제거
     - Totally allocation을 일반화한 방법 & 자원들에게 순서를 부여 : 가능은 하지만 비효율적
     - **프로세스는 순서의 증가 방향으로만 자원 요청 가능** => 자원 낭비 발생

   <br/>

2. Deadlock 회피법

   - 시스템을 항상 **safe state**로 유지 : 시스템의 상태를 **계속 감시**하다가, deadlock 상태가 될 가능성이 있으면 **자원 할당 요청 보류**한다. 
     - High overhead : 항상 시스템 감시하기 때문
     - Low resource utilization : Safe state 유지를 위해 사용되지 않는 자원 존재
     - Not practical : (가정) 프로세스 수, 자원 수가 고정. 필요한 최대 자원 수를 알고 있음
   - safe state란?
     - Safe state : 모든 프로세스가 정상적 종료 가능한 상태 = **Safe sequence가 존재**
     - Unsafe state : Deadlock 상태가 될 **가능성이 있음**. 반드시 발생한다는 의미는 X
   - Deadlock Avoidance 의 가정 4가지
     - 프로세스의 수가 고정. 
     - 자원의 종류와 수가 고정. 
     - 프로세스가 요구하는 자원 및 최대 수량을 알고 있음. 
     - 프로세스는 자원을 사용 후 반드시 반납
   - Dijkstra's banker's algorithm
     - **한 종류의 자원**이 여러개. 시스템을 항상 safe state로 유지.
     - 현재 상태에서 안전 순서가 하나 이상 존재하면 안전 상태
     - 임의의 순간에 프로세스들이 모두, 가지고 있는 단위 자원 이상을 요청하는 경우 시스템은 교착상태에 놓이게 됨.
     - 자원 요청이 들어오면 그 **자원을 주었다고 가정**하고, 시뮬레이션을 해본다. 시뮬레이션 결과 **safe sequence가 존재하면 자원을 주고** 존재하지 않으면 거절한다.
   - Habermann's algorithm (다익스트라 알고리즘의 확장)
     - **여러 종류의 자원**. 시스템을 항상 safe state로 유지.
     - 자원의 종류만 다르고, 다익스트라 알고리즘과 동일한 매커니즘 

   <br/>

3. Deadlock 탐지법

   - Deadlock 탐지 및 복구법

     - Deadlock 방지를 위한 사전 작업 X
     - 주기적으로 Deadlock 발생 확인 => **Resource Allocation Graph (RAG) 사용**

   - Resource Allocation Graph (RAG)

     - Deadlock 검출을 위해 사용. Directed, bipartite Graph
     - G = (Node, Edge) 
       - N (Node) = {Np, Nr} . Np : 프로세서들의 집합. Nr : 리소스들의 집합
       - E (Edge) 는 Np와 Nr 사이에만 존재. 
     - Rk : k type의 자원 & tk : Rk의 단위 자원 수가 몇 개인지 & |(a, b)| : (a, b) edge의 수

     <img src="chap7 교착상태.assets/image-20210822184125422.png" alt="image-20210822184125422" style="zoom:67%;" />

   - Graph reduction : **주어진 RAG에서 edge를 하나씩 지워가는 방법**

     - edge 제거 여부에 따라
       - Completely reduced : 모든 edge가 제거됨 => 데드락에 빠진 프로세스 X
       - Irreducible : 지울 수 없는 edge가 존재 => 하나 이상의 프로세스가 데드락 상태
     - Graph reduction procedure
       - Unblocked process : 필요한 자원을 모두 할당 받을 수 있는 프로세스.
       - **더이상 Unblocked process가 없을 때까지** Unblocked process에 연결된 모든 **edge를 제거**한다. 최종 Graph에서 모든 edge가 제거(데드락X)되거나 일부 edge가 남는다(데드락) 
     - Graph Reduction
       - High overhead : 검사 주기에 영향을 받음. Node의 수가 많은 경우.
       - Low overhead 데드락 탐지법 (special case)
         - case 1) Single-unit resources
         - case 2) Single-unit request in expedient state

   - 데드락 회피 vs 탐지
     - 데드락 회피 : 최악의 경우를 생각. 데드락이 발생X
     - 데드락 탐지 : 최선의 경우만 생각. 데드락 발생시 복구 과정이 필요

   <br/>

4. 데드락 복구법

   - Process termination : 데드락 상태인 프로세스 중 일부 종료
     - Termination cost model : 종료시킬 데드락 상태의 프로세스 선택. 우선순위, 종류, 총 수행 시간, 남은 수행 시간, 종료 비용 등
     - 최소 종료 비용 프로세스를 선택 : 간단. 낮은 오버헤드. 불필요한 프로세스들이 종료될수도.
     - 최소 비용 복구 프로세스를 선택 : 모든 경우의 수를 고려하여 최소 비용으로 데드락 상태를 해소할 수 있는 프로세스 선택. 족잡. 높은 오버헤드.
   - Resource preemption : 데드락 상태 해결을 위해 선점할 자원 선택하고, 해당 자원 가진 프로세스를 종료
     - 데드락 상태가 아닌 프로세스가 종료될수도. (해당 프로세스는 이후 재시작 됨)
     - Preemption cost model : 선점할 자원 선택. 최소 비용 복구법을 사용
   - Checkpoint-restart method
     - 프로세스의 수행 중 특정 지점마다 context를 저장. Rollback을 위해 사용 (checkpoint)