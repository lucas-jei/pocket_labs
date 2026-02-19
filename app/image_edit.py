import os
import shutil

from PIL import Image
from pathlib import Path


running_type = int(input("1:이미지 생성부터 진행, 2:패키지 생성부터 진행"))

if(running_type == 1):

    input_folder = "source_img"
    output_folder_1 = "01_bg"
    output_folder_2 = "02_thumbnail"

    target_width_1 = int(input("배경이미지의 가로사이즈(숫자)를 입력하세요"))
    target_width_2 = int(input("썸네일의 가로사이즈(숫자)를 입력하세요"))

    os.makedirs(output_folder_1, exist_ok=True)
    os.makedirs(output_folder_2, exist_ok=True)


    img_number = 1
    for file in os.listdir(input_folder):

        if file.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".webp")):

            if img_number==1:
                print("이미지 변환을 진행 중입니다. 잠시만 기다려 주십시오.")

            path = os.path.join(input_folder, file)
            name = os.path.splitext(file)[0]
            new_name = f"img_{img_number:02}"

            # ================= BG =================
            img_bg = Image.open(path)

            w, h = img_bg.size
            new_height = int(h * (target_width_1 / w))

            img_bg = img_bg.resize((target_width_1, new_height), Image.LANCZOS)
            img_bg = img_bg.convert("RGB")

            out_path = os.path.join(output_folder_1, new_name + ".jpg")
            img_bg.save(out_path, "JPEG", optimize=True, quality=95)


            # ================= THUMB =================
            img_thumb = Image.open(path)

            w, h = img_thumb.size
            new_height = int(h * (target_width_2 / w))

            img_thumb = img_thumb.resize((target_width_2, new_height), Image.LANCZOS)
            img_thumb = img_thumb.convert("RGBA")

            out_path = os.path.join(output_folder_2, new_name + ".png")
            img_thumb.save(out_path, "PNG", optimize=True)

        img_number += 1

    print("이미지 변환이 완료되었습니다.")

elif running_type == 2:

    # ===== 변수 설정 =====
    PROJECT_PREFIX = input("패키지명을 입력하세요.")

    SOURCE = Path("./package_source")
    DEST_BASE = Path("./package_result")
    IMAGE_SRC = Path("./01_bg")
    THUMBNAIL_SRC = Path("./02_thumbnail")
    IMAGE_PREFIX = "img"

    package_type = int(input("1: 선택형(슬라이드 번호 수동입력), 2: 연속형(슬라이드 시작과 끝을 입력) 1 / 2 중 선택하세요."))

    if(package_type == 1):

        SLIDE_NUM = list(map(int, input("슬라이드 번호(숫자만 입력)를 구분자 콤마(,)를 사용하여 입력하세요").split(",")))

        def copy_tree_e(src: Path, dst: Path) -> None:
            """robocopy /E 수준: 하위 폴더 포함 전체 복사(기존 폴더 있으면 병합/덮어쓰기)."""
            for root, dirs, files in os.walk(src):
                root_p = Path(root)
                rel = root_p.relative_to(src)
                target_dir = dst / rel
                target_dir.mkdir(parents=True, exist_ok=True)

                # 빈 폴더 포함: dirs는 자동으로 target_dir 생성으로 커버됨
                for f in files:
                    s = root_p / f
                    d = target_dir / f
                    shutil.copy2(s, d)  # 메타데이터 유지

        for n in SLIDE_NUM:
            print(f"==== {n:02} 패키지 생성 시작 ====")

            project_dir = DEST_BASE / f"{PROJECT_PREFIX}_{n:02}"

            # 1) /E 수준 폴더 전체 복사
            copy_tree_e(SOURCE, project_dir)

            # 2) bg 이미지 복사 + 이름 고정(bg.jpg)
            (project_dir / "images").mkdir(parents=True, exist_ok=True)
            shutil.copy2(IMAGE_SRC / f"{IMAGE_PREFIX}_{n:02}.jpg",
                         project_dir / "images" / "bg.jpg")

            # 3) thumbnail 복사 + 이름 고정(thumb.png)
            shutil.copy2(THUMBNAIL_SRC / f"{IMAGE_PREFIX}_{n:02}.png",
                         project_dir / "thumb.png")

        print("패키지 생성 완료")

    elif package_type == 2:

        SLIDE_START = int(input("시작 페이지를 입력하세요(숫자만 입력 가능)"))
        SLIDE_END = int(input("종료 페이지를 입력하세요(숫자만 입력 가능)"))


        def copy_tree_e(src: Path, dst: Path) -> None:
            """robocopy /E 수준: 하위 폴더 포함 전체 복사(기존 폴더 있으면 병합/덮어쓰기)."""
            for root, dirs, files in os.walk(src):
                root_p = Path(root)
                rel = root_p.relative_to(src)
                target_dir = dst / rel
                target_dir.mkdir(parents=True, exist_ok=True)

                # 빈 폴더 포함: dirs는 자동으로 target_dir 생성으로 커버됨
                for f in files:
                    s = root_p / f
                    d = target_dir / f
                    shutil.copy2(s, d)  # 메타데이터 유지


        for n in range(SLIDE_START, SLIDE_END + 1):
            print(f"==== {n:02} 패키지 생성 시작 ====")

            project_dir = DEST_BASE / f"{PROJECT_PREFIX}_{n:02}"

            # 1) /E 수준 폴더 전체 복사
            copy_tree_e(SOURCE, project_dir)

            # 2) bg 이미지 복사 + 이름 고정(bg.jpg)
            (project_dir / "images").mkdir(parents=True, exist_ok=True)
            shutil.copy2(IMAGE_SRC / f"{IMAGE_PREFIX}_{n:02}.jpg",
                         project_dir / "images" / "bg.jpg")

            # 3) thumbnail 복사 + 이름 고정(thumb.png)
            shutil.copy2(THUMBNAIL_SRC / f"{IMAGE_PREFIX}_{n:02}.png",
                         project_dir / "thumb.png")

        print("패키지 생성 완료")