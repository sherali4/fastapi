from aiogram.dispatcher.filters.state import State, StatesGroupclass tovar_reg(StatesGroup):    turi = State()    name = State()    ulchov = State()    narx = State()    tarifi = State()    photo = State()class del_tovar(StatesGroup):    id = State()class plus_admin(StatesGroup):    user_id = State()    ifo = State()    tovar_turi = State()    menyu = State()class del_admin(StatesGroup):    id_user = State()class add_tovar_turi_admin(StatesGroup):    nomi = State()    izohi = State()class del_tovar_turi_admin(StatesGroup):    nomi = State()class user_reg(StatesGroup):    name = State()    numb = State()class narxini_uzgartirish(StatesGroup):    id = State()    narx = State()