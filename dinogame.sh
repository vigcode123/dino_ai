if ! test -d ./venv ; then
  echo "venv does not exist. making new one"
  python3 -m venv venv
fi

. venv/bin/activate

pip3 install -r requirements.txt

if ! [ ./winner.pkl ]; then
  echo -n “Enter Num Cores: “
  read x

  if ! [ ./checkpoint]; then
    python3 gym_solver.py --num-cores=x
  else
    python3 gym_solver.py --checkpoint checkpoint --num-cores=x
  fi
else
  python3 gym_best.py
fi
