import os
import shutil
import subprocess
from pdf2image import convert_from_path

# paths
desktop_dir = os.path.join(os.path.expanduser('~'), "Desktop")
source_dir = os.path.join(desktop_dir, "Resume Automated")
website_dir = os.path.join(os.path.expanduser('~'), 'vscode', 'personal_website_2')  # directory for my website repo
resume_dir = os.path.join(website_dir, 'public', 'resume')  # final directory

# new filenames
new_resume_filename = "raglandconnor_resume.pdf"
new_png_filename = "raglandconnor-resume-img.png"

# new paths
resume_dest = os.path.join(resume_dir, new_resume_filename)
png_dest = os.path.join(resume_dir, new_png_filename)

# git commands
git_add = ["git", "add", resume_dest, png_dest]
git_commit = ["git", "commit", "-m", "Update resume (script)"]
git_push = ["git", "push", "origin", "main"]  # push to remote main branch

def find_pdf_file(directory):  # find first PDF file in directory
    for file_name in os.listdir(directory):
        if file_name.endswith('.pdf'):
            return file_name
    return None

resume_filename = find_pdf_file(source_dir)

# if new resume exists
if resume_filename:
    resume_src = os.path.join(source_dir, resume_filename)

    # convert to pdf
    images = convert_from_path(resume_src)

    if images:
        # save as pdf in project repository
        png_src = os.path.join(resume_dir, new_png_filename) 
        images[0].save(png_dest, 'PNG')

        # move files
        shutil.move(resume_src, resume_dest)
        shutil.move(png_src, png_dest)

        print(f"""Files moved to: 
              resume: {resume_dest}
              png: {png_dest}""")
        
        os.chdir(website_dir)

        # run git commands
        try:
            subprocess.run(git_add)
            subprocess.run(git_commit)
            subprocess.run(git_push)

            print("Changes pushed to remote repository.")
        except Exception as e:
            print(f"An error occurred when performing git commands: {e}")

    else:
        print('Failed to convert PDF to PNG.')

# no new resume exists 
else:
    print(f"PDF file does not exist in the source directory: {source_dir}")