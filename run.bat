@echo off

pushd %CD%

mkdir cached
cd cached
mkdir en
mkdir links
for %%d in (cs ct de es fr it jp kr pt ru) do mkdir %%d
cd links
for %%d in (cs ct de es fr it jp kr pt ru) do mkdir %%d

popd

call env.bat
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

