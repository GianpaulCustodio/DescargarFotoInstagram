import instaloader
import requests

def download_instagram_profile_picture(username):
    # Crear una instancia de Instaloader
    L = instaloader.Instaloader()

    try:
        # Obtener el perfil
        profile = instaloader.Profile.from_username(L.context, username)
        
        # Obtener la URL de la foto de perfil en alta resolución
        profile_pic_url = profile.profile_pic_url

        # Descargar la foto de perfil
        response = requests.get(profile_pic_url)

        if response.status_code == 200:
            with open(f"{username}.jpg", "wb") as file:
                file.write(response.content)
            print(f"La foto de perfil de {username} ha sido descargada exitosamente en alta resolución.")
        else:
            print(f"No se pudo descargar la foto de perfil de {username}.")
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"La cuenta {username} no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    username = input("Introduce el nombre de usuario de Instagram: ")
    download_instagram_profile_picture(username)
