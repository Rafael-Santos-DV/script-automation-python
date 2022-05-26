from time import sleep

def InformationOfAnime() -> dict[str, any]:
    gender: list[str] = [];
    episodesList: list[dict[str]] = [];

    server: str = input("Your server url of anime: ").strip();
    anime: str = input("Give the name of the anime: ").strip();
    episodePoster: str = input("Your server url of episode poster: ").strip();
    likes: float = float(input("Feedback of anime: ").strip());
    poster: str = input("Poster URL: ").strip();
    episodes: int = int(input("Number of episodes: "));
    description: str = input("Description of the anime: ").strip();
    year: str = input("Year of the anime: ").strip();
    
    inputGender = "";

    while (inputGender.upper() != "N"):
        inputGender: str = input("Add a gender? #inform 'n' to leave# -> ");
        if (len(inputGender.strip()) > 0 and inputGender.upper() != "N"):
            gender.append(inputGender);
            print("add sucess");

    print("I'am generating your episodes :");
    print("Await...");
    sleep(1);

    for c in range(0, episodes):
        episodesList.append({
            "title": f"episodio {c+1}",
            "url": f"{server}/{f'0{c+1}' if(len(str(c+1)) < 2) else c+1}.mp4"
        });

    print("generate with sucess!");

    return {
        "anime": anime,
        "likes": likes,
        "poster": "https://image.tmdb.org/t/p/original"+poster,
        "quant": episodes,
        "description": description,
        "ano": year,
        "gender": gender,
        "episodes": episodesList,
        "episodePoster": "https://image.tmdb.org/t/p/original"+episodePoster
    };
