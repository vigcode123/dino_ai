if ! test -d ./venv ; then
  echo "venv does not exist. making new one"
  python3 -m venv venv
fi

. venv/bin/activate

pip3 install -r requirements.txt


if ! test -f ./DinoGame/model/winner.pkl ; then
  read -p "Enter Num Cores:" x
  echo Setting Number of Cores as $x

  if ! test -f ./DinoGame/model/checkpoint ; then
    python3 ./DinoGame/gym_solver.py --num-cores=$x
  else
<<<<<<< HEAD
    python3 ./DinoGame/gym_solver.py --checkpoint model/checkpoint --num-cores=$x
=======
    python3 ./DinoGame/gym_solver.py --checkpoint ./DinoGame/model/checkpoint --num-cores=$x
>>>>>>> ec1e62c (fixed pathing issues)
  fi
else
  python3 ./DinoGame/gym_best.py
fi
