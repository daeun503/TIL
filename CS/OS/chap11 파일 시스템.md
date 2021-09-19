# chap11 파일 시스템

## Disk System

1. Disk pack
   - 데이터 영구 저장 장치 (비휘발성)
   - 구성 : Sector, Track, Cylinder, Platter, Surface
   
   <img src="chap11 파일 시스템.assets/image-20210919194709081.png" alt="image-20210919194709081" style="zoom:67%;" />
   
2. Disk drive
   
   <img src="chap11 파일 시스템.assets/image-20210919194726024.png" alt="image-20210919194726024" style="zoom:67%;" />
   
   - Disk pack 에 데이터를 기록하거나 판독할 수 있도록 구성된 장치
   - 구성 : Head, Arm, Positioner (boom), Spindle
   
3. Disk Address
   - Physical disk address
     - Sector 를 지정하려면 => Cylinder number,  Surface Number, Sector Number를 알아야 함
   - Logical disk address : relative address
     - Disk system의 데이터 전체를 **번호가 부여된 block**들의 나열로 취급 
     - block 번호 => physical address 모듈 필요 (d isk driver)
   - OS는 disk의 block 번호 전달 => Disk driver가 전달 받은 block 번호를 실제 disk의 Physical Address로 변환 => disk controller가 실제 disk의 해당 영역으로 찾아가 데이터를 쓰거나 읽음

4. Data Access in Disk System

   - Seek time : disk head를 필요한 cylinder로 이동시키는 시간
   - Rotational delay : seek time 이후, 필요한 sector가 head 위치로 도착하는 시간
   - Data transmission time : rotational delay 이후, 해당 sector를 읽어서 전송하는 시간
   - Data Access time : Seek time + Rotational delay + Data transmission time

<br/>

## File System

1. File System
   - 사용자들이 사용하는 파일들을 관리하는 운영체제의 한 부분
   - 구성 : Files, Directory structure, Partitions
2. File Concept
   - File : 보조 기억 장치에 저장된 연관된 정보들의 집합
     - 보조 기억 장치 할당의 최소 단위. Sequence of bytes (물리적 정의)
     - 내용에 따른 분류 : Program file / Data file
     - 형태에 따른 분류 : Text file / Binary file
   - OS 는 file operation들에 대한 system call을 제공해야한다.
     - file operations : Create, Write, Read, Delete, Reposition 등
3. File Access Methods
   - Sequential access (순차 접근) : File을 record 단위로 순서대로 접근
   - Directed access (직접 접근) : 원하는 Block을 직접 접근
   - Indexed access : Index를 참조하여, 원하는 block을 찾은 후 데이터에 접근
4. File System Organiztion
   - Partitions (minidisks, volumnes) : Virtual disk
   - Directory : File들을 분류, 보관하기 위한 개념
     - Operations on directory (Create, Delete, Rename 등)들은 OS가 system call을 통해 제공
5. File System Organization
   - Mounting : 현재 FS(File System)에 다른 FS를 붙이는 것

<br/>

## Directory Structure

1. Logical directory structure
   - Flat (single-level) directory structure
   - 2-level directory structure
   - Hierarchical (tree-structure) directory structure
   - Acyclic graph directory structure
   - General graph directory structure
2. Flat Directory Structure
   - FS내에 **하나의 directory만** 존재 (계층 X)
   - 문제점 : File naming, File protection, File management 등
3. 2-level directory structure
   - **사용자마다 하나**의 directory 배정
   - 구조 : MFD (Master File Directory) / UFD (User File Directory)
   - 문제점 : Sub-directory 생성 불가, 사용자간 파일 공유 불가 
4. Hierarchical directory structure
   - **Tree 형태**의 계층적 directory 사용 가능 (대부분의 OS 가 사용)
   - 사용자가 하부 directory 생성/관리 가능 (system call 이 제공)
5. Acyclic Graph directory structure
   - Hierarchical directory structure의 확장 (사이클 허용 X)
   - Directory 안에 shared directory, shared file을 담을 수 있음
   - Link의 개념 사용 => 바로가기 아이콘 st
6. General Graph directory structure
   - Acyclic Graph directory structure의 일반화 (사이클 허용)
   - 문제점 : File 탐색시, infinite loop를 고려해야 함

<br/>

## File Protection

1. File Protection : File에 대한 부적절한 접근 방지

   - 접근 제어가 필요한 연산 : Read(R) , Write(W) , Execute(X) , Append(A)

2. File Protection Mechanism

   - 파일 보호 기법은 system size 및 응용 분야에 따라 다를 수 있음

   - Password 기법 : 각 file들에 PW 부여 => 비현실적

     - 모든 파일에 대한 PW를 기억하기 불가능 & 접근 권한 별로 서로 다른 PW를 부여해야 함

   - Access Matrix 기법 

     - 범위(domain = 사용자, 프로세스)와 개체(object = 접근 대상, 파일) 사이의 접근 권한 명시

     <img src="chap11 파일 시스템.assets/image-20210919204056566.png" alt="image-20210919204056566" style="zoom:67%;" />

     - Global Table : 시스템 전체 **file들에 대한 권한을 Table로** 유지.
       - 간단하지만 큰 table size로 용량 커짐
     - Access list : Access matrix의 **column을 list로** 표현. 실제 OS에서 많이 사용됨
       - 각 object(파일)에 대한 접근 권한을 나열 => A(Fk) = {<D1,R1>, <D2, R2> ... }
       - 모든 접근마다 권한을 검사해야 함 => object 많이 접근하는 경우 느려짐
     - Capability list : Access matrix의 **row를 list로** 표현
       - 각 domain(사용자)에 대한 접근 권한을 나열 => C(D1) = {<F1, R1>, <F2, R2> ... }
       - 시스템이 capabilty list자체를 보호해야 하므로, kernel 안에 저장
       - object별 권한 관리 (권한 취소 등) 가 어려움
     - Locak-key mechanism : Access list + Capability list 
       - Object는 Lock을, Domain은 Key를 가지며, 시스템은 key list를 관리해야 한다.
       - domain내의 프로세스가 object에 접근 시, 자신의 key와 object의 lock이 맞아야 한다.
     - 많은 OS가 Access list + Capability list를 사용
       - Object에 대한 첫 접근 => access list로 탐색하고 Capability 생성 후 해당 프로세스에게 전달
       - 마지막 접근 후 => Capability 삭제

<br/>

## Allocation Methods

1. Continuous allocation
   - 한 file을 디스크의 **연속된 block에 저장**. 효율적인 file 접근(순차, 직접 접근)
   - 문제점
     - 새로운 file을 위한 공간 확보 어려움 => External fragmentation
     - file 공간 크기 결정이 어려움. **파일이 커져야하는 경우를 고려**해야 하는데 어려움
2. Discontinuous allocation - Linked allocation
   - file이 저장된 block들을 **linked list로 연결**. 간단하고 Exteranl fragmentation X
     - Directory는 각 file에 대한 첫번째 block에 대한 포인터를 가진다.
     - File Allocation Table (FAT) : 각 block의 **시작 부분에 다음 블록의 번호를** 기록
   - 문제점
     - 직접 접근에 비효율적
     - 포인터 저장을 위한 추가적인 공간 필요
     - 신뢰성 문제 : 사용자가 포인터를 실수로 건드렸을 때 파일을 사용할 수 없게 됨
3. Discontinuous allocation - Indexed Allocation
   - File이 저장된 block의 정보(pointer)를 index block에 모아 둠
     - 직접 접근에 효율적 (목차st) , 순차 접근에는 비효율적
   - 문제점 => File 당 index block을 유지해야 함
     - index block을 위한 추가 공간 필요. space overhead
     - index block 크기에 따라 파일의 최대 크기가 제한됨

<br/>

## Free Space Management

1. Bit vector
   - 시스템 내 모든 block 들에 대한 **사용 여부를 1 bit flag로** 표시. 간단하고 효율적
   - Bit vector 전체를 메모리에 보관해야 함 => 공간이 많이 필요해서 대형 시스템에 부적합
2. Linked List
   - **빈 block을 linked list로** 연결. 비효율적 (일일이 하나씩 링크를 따라가야 하기 때문)
3. Grouping
   - n개의 빈 block을 그룹으로 묶고, **그룹 단위로 linked list**로 연결
   - 연속된 빈 block을 쉽게 찾을 수 있음
4. Counting
   - 연속된 빈 block들 중 **첫 번째 block의 주소와 연속된 block의 수를 table**로 유지
   - Continuous allocation 시스템에 유리한 기법

