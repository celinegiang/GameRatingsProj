// Compile:  g++ -std=c++17 GameRatings.cpp -o gameratings
// Run:      ./gameratings

#include <iostream>
#include <map>
#include <string>

class GameRatings {
public:
   
    bool rate(const std::string& user, const std::string& game, int score) {
        if (score < 1 || score > 5) return false;
        ratings_[game][user] = score;  // rating again just overwrites
        return true;
    }

    double average(const std::string& game) const {
        auto it = ratings_.find(game);
        if (it == ratings_.end() || it->second.empty()) return 0.0;
        int total = 0;
        for (const auto& entry : it->second) total += entry.second;
        return static_cast<double>(total) / it->second.size();
    }

    int getRating(const std::string& user, const std::string& game) const {
        auto g = ratings_.find(game);
        if (g == ratings_.end()) return 0;
        auto u = g->second.find(user);
        return (u == g->second.end()) ? 0 : u->second;
    }

    void printAll() const {
        for (const auto& game : ratings_) {
            std::cout << game.first << " (avg " << average(game.first) << ")\n";
            for (const auto& entry : game.second) {
                std::cout << "  " << entry.first << ": " << entry.second << "/5\n";
            }
        }
    }

private:
    std::map<std::string, std::map<std::string, int>> ratings_;
};

int main() {
    GameRatings box;

    box.rate("celine", "Hades", 5);
    box.rate("friend", "Hades", 4);
    box.rate("celine", "Celeste", 5);
    box.rate("friend", "Celeste", 3);
    box.rate("friend", "Celeste", 4);  // updates the earlier 3

    if (!box.rate("celine", "Hades", 9)) {
        std::cout << "Rejected: score must be 1-5\n\n";
    }

    box.printAll();
    return 0;
}