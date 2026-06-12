# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 20602 구승연
# 프로젝트 주제: 
def show_menu():
    """프로그램 메뉴를 보여주는 함수"""
    print("\n======================================")
    print("      ✨ 나만의 주도적 학습 메이트 ✨      ")
    print("======================================")
    print("1. 과목별 학습 상태 및 단원 설정")
    print("2. 오늘의 맞춤형 공부 방법 및 피드백 확인")
    print("3. 프로그램 종료")
    print("======================================")


def init_subjects(subject_data):
    """과목별 단원명과 학습 진행 정도(1~5)를 입력받는 함수"""
    print("\n--- 📝 과목별 현재 학습 상태 입력 ---")
    
    # 2차원 리스트의 각 행(과목)을 돌면서 입력을 받습니다.
    for i in range(len(subject_data)):
        subject_name = subject_data[i][0]  # 국어, 수학, 영어
        print(f"\n[{subject_name}]에 대한 정보를 입력하세요.")
        
        # 1. 현재 공부 중인 단원명 입력
        unit = input("현재 학습 중인 단원명을 입력하세요 (예: 등차수열): ")
        subject_data[i][1] = unit
        
        # 2. 학습 진행 정도 입력 (예외 처리/데이터 검증 포함)
        while True:
            progress_str = input("나의 학습 진행 정도를 입력하세요 (1부터 5까지): ")
            
            # 정교화 포인트: 숫자가 맞는지 검사
            if progress_str.isdigit(): 
                progress = int(progress_str)
                if 1 <= progress <= 5:
                    subject_data[i][2] = progress
                    break  # 올바른 범위면 반복문 탈출
                else:
                    print("⚠️ 경고: 1부터 5 사이의 숫자만 입력할 수 있습니다.")
            else:
                print("⚠️ 경고: 숫자만 입력해 주세요.")
                
    print("\n✅ 모든 과목의 초기 설정이 완료되었습니다!")


def analyze_and_feedback(subject_data):
    """입력된 데이터를 바탕으로 시간 계산 및 맞춤형 피드백을 출력하는 함수"""
    print("\n--- 📊 오늘의 맞춤형 학습 분석 리포트 ---")
    
    for i in range(len(subject_data)):
        subject_name = subject_data[i][0]
        unit_name = subject_data[i][1]
        progress = subject_data[i][2]
        
        # 아직 설정을 안 했다면 건너뛰기
        if unit_name == "미설정" or progress == 0:
            print(f"\n❌ [{subject_name}] 아직 학습 상태가 설정되지 않았습니다. 1번 메뉴를 먼저 실행하세요.")
            continue
            
        print(f"\n======================================")
        print(f"📖 [{subject_name} - {unit_name}] 분석 결과 (진행도: {progress}/5)")
        print(f"======================================")
        
        # [정교화 공식] 1~5 단계에 따른 공부 시간과 복습 시간 계산
        # 진행도가 낮을수록 기본 공부 시간이 길고, 진행도가 높을수록 복습에 집중하도록 유도
        study_time = (6 - progress) * 20 + 20  # 예: 2단계면 (4)*20+20 = 100분
        review_time = (progress * 10) + 10     # 예: 2단계면 (2)*10+10 = 30분
        
        print(f"🎯 추천 공부 시간: {study_time}분")
        print(f"🔄 추천 복습 시간: {review_time}분")
        print("-" * 38)
        
        # 사용자의 학습 희망 선택 받기
        print("오늘 더 집중하고 싶은 학습 유형을 선택하세요.")
        print("1. 기본학습  2. 유형학습  3. 심화학습")
        choice = input("선택 (1~3): ")
        print("-" * 38)
        
        ### 💡 [학생 미션] 과목별/선택별 피드백 로직 채우기 ###
        # 우리가 약속한 규칙에 따라 if-elif-else 구조를 완성해 보세요!
        
        if subject_name == "수학":
            if choice == "1":    # 기본학습
                # 1~2단계와 3~4단계, 5단계를 묶어서 출력하거나 공식을 활용해 보세요.
                print("💡 [피드백] 현재 단원의 기본 개념 공식과 원리를 먼저 눈으로 익혀야 할 때입니다.")
                # 문제 수 계산 공식 예시
                question_count = (6 - progress) * 4
                print(f"📝 [미션] 교과서 예제 수준의 기초 문제를 {question_count}개 정확하게 푸세요!")
                
            elif choice == "2":  # 유형학습
                print("💡 [피드백] 시험에 자주 나오는 대표 유형들을 정복할 차례입니다.")
                pass # 이 부분을 직접 채워보세요!
                
            elif choice == "3":  # 심화학습
                pass # 이 부분을 직접 채워보세요!
                
            else:
                print("⚠️ 올바른 학습 유형 번호가 아닙니다.")
                
        else:  # 국어, 영어 등 타 과목 (개념 숙지 중심)
            if choice == "1":    # 기본학습
                print("💡 [피드백] 단원의 전체적인 흐름과 핵심 키워드를 파악하는 것이 가장 중요합니다.")
                read_count = (6 - progress) // 2 + 1
                print(f"📝 [미션] 교과서나 텍스트를 기본 개념 {read_count}회독하며 소리 내어 읽어보세요.")
                
            elif choice == "2":  # 유형학습
                pass # 이 부분을 직접 채워보세요!
                
            elif choice == "3":  # 심화학습
                pass # 이 부분을 직접 채워보세요!
                
            else:
                print("⚠️ 올바른 학습 유형 번호가 아닙니다.")


def main():
    # 2차원 리스트 구조 정의: [과목명, 현재단원, 진행정도(1~5)]
    # 초기값은 미설정 상태로 시작합니다.
    subject_data = [
        ["국어", "미설정", 0],
        ["수학", "미설정", 0],
        ["영어", "미설정", 0]
    ]
    
    while True:
        show_menu()
        choice = input("원하는 메뉴 번호를 선택하세요: ")
        
        if choice == '1':
            init_subjects(subject_data)
        elif choice == '2':
            analyze_and_feedback(subject_data)
        elif choice == '3':
            print("\n프로그램을 종료합니다. 오늘도 주도적으로 열공하세요! 🔥")
            break
        else:
            print("⚠️ 올바른 번호를 입력해 주세요. (1~3)")


if __name__ == "__main__":
    main()