# Loss

Funkcja straty, znana również jako funkcja kosztu, uwzględnia prawdopodobieństwo lub niepewność prognozy na podstawie tego, jak bardzo prognoza różni się od wartości prawdziwej. Daje nam to bardziej zniuansowany obraz tego, jak dobrze działa model.
W przeciwieństwie do dokładności, strata jest sumą błędów popełnionych dla każdej próbki w zbiorach uczących lub walidacyjnych. Strata jest często wykorzystywana w procesie uczenia w celu znalezienia „najlepszych” wartości parametrów dla modelu (np. wag w sieci neuronowej). Podczas procesu szkoleniowego celem jest zminimalizowanie tej wartości.
W przeciwieństwie do dokładności, strata może być stosowana zarówno w problemach z klasyfikacją, jak i regresją.

# Accuracy

Dokładność to metoda pomiaru wydajności modelu klasyfikacyjnego. Zazwyczaj wyraża się ją w procentach. Dokładność to liczba przewidywań, w których przewidywana wartość jest równa prawdziwej wartości. Jest binarny (prawda/fałsz) dla określonej próbki. Dokładność jest często przedstawiana na wykresie i monitorowana podczas fazy uczenia, chociaż wartość jest często powiązana z ogólną lub ostateczną dokładnością modelu. Dokładność jest łatwiejsza do interpretacji niż strata.

## Binary
Oblicza, jak często podpowiedzi pasują do etykiet binarnych.
## Categorical
Oblicza, jak często podpowiedzi pasują do najgorętszych etykiet.
# AUC
"Area under the curve" - pole pod krzywą

Obszar pod krzywą (AUC) jest miarą zdolności klasyfikatora do rozróżniania klas i jest używany jako podsumowanie krzywej ROC.

Im wyższy AUC, tym lepsza wydajność modelu w rozróżnianiu klas pozytywnych i negatywnych.

Gdy AUC = 1, klasyfikator jest w stanie doskonale rozróżnić wszystkie punkty klasy dodatniej i ujemnej. Gdyby jednak AUC było 0, klasyfikator przewidywałby wszystkie negatywne jako pozytywne, a wszystkie pozytywne jako negatywne.

# Mean absolute error
Błąd bezwględny. W kontekście uczenia maszynowego odnosi się do wielkości różnicy między przewidywaniem obserwacji a prawdziwą wartością tej obserwacji. MAE przyjmuje średnią błędów bezwzględnych dla grupy przewidywań i obserwacji jako miarę wielkości błędów dla całej grupy. MAE można również określić jako funkcję straty L1.

Jako jedna z najczęściej używanych funkcji straty w problemach regresji, MAE pomaga użytkownikom przekształcić problemy uczenia się w problemy optymalizacji. Służy również jako łatwy do zrozumienia kwantyfikowalny pomiar błędów dla problemów regresji.


# Poisson

Oblicza metrykę Poissona między y_true i y_pred. Funkcja straty Poissona jest używana do regresji podczas modelowania danych liczbowych. Użycie dla danych jest zgodne z rozkładem poissona. Np. odpływ klientów w przyszłym tygodniu. Minimalizacja straty Poissona jest równoważna maksymalizacji prawdopodobieństwa danych przy założeniu, że cel pochodzi z rozkładu Poissona, uwarunkowanego danymi wejściowymi.