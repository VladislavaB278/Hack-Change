import trackList from "../src/assets/trackLinks";
import style from "./mainPage.module.scss";

const MainPage = () => {
  return (
    <div className={style.search}>
      <>Поиск треков</>
      <div className={style.list}>
        {trackList.map((track) => (
          // eslint-disable-next-line react/jsx-key
          <div>{JSON.stringify(track)}</div>
        ))}
      </div>
    </div>
  );
};

export default MainPage;
