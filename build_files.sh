echo " BUILD START"
python3.12  -m pip install -r requirements.txt
python3.12 manage.py collectstatic --noinput && vercel build
echo " BUILD END"