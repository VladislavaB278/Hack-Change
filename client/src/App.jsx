import MainPage from "./pages/MainPage/MainPage";
import Playbar from "./components/Playbar/Playbar";
import style from "./global.module.scss";
import Register from "./components/Reg/register"



const App = () => (
  <div className={style.wrapper}>
    <MainPage />
    <Playbar />
    <Register />
</div>
);

export default App;

